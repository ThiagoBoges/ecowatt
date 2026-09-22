from collections import defaultdict
from datetime import date

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Alert, Reading, Room
from .schemas import AlertOut, ReadingCreate, ReadingOut, ReportOut, RoomCreate, RoomOut, RoomUpdate
from .services import build_alert, classify_consumption

app = FastAPI(title="EcoWatt API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"], allow_methods=["*"], allow_headers=["*"])


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health(): return {"status": "ok"}


@app.post("/api/v1/rooms", response_model=RoomOut, status_code=201)
def create_room(payload: RoomCreate, db: Session = Depends(get_db)):
    if db.scalar(select(Room).where(Room.name == payload.name)):
        raise HTTPException(409, "Já existe uma sala com este nome.")
    room = Room(**payload.model_dump()); db.add(room); db.commit(); db.refresh(room); return room


@app.get("/api/v1/rooms", response_model=list[RoomOut])
def list_rooms(db: Session = Depends(get_db)):
    return db.scalars(select(Room).order_by(Room.name)).all()


@app.get("/api/v1/rooms/{room_id}", response_model=RoomOut)
def get_room(room_id: int, db: Session = Depends(get_db)):
    room = db.get(Room, room_id)
    if not room: raise HTTPException(404, "Sala não encontrada.")
    return room


@app.put("/api/v1/rooms/{room_id}", response_model=RoomOut)
def update_room(room_id: int, payload: RoomUpdate, db: Session = Depends(get_db)):
    room = db.get(Room, room_id)
    if not room: raise HTTPException(404, "Sala não encontrada.")
    for field, value in payload.model_dump().items(): setattr(room, field, value)
    db.commit(); db.refresh(room); return room


@app.delete("/api/v1/rooms/{room_id}", status_code=204)
def delete_room(room_id: int, db: Session = Depends(get_db)):
    room = db.get(Room, room_id)
    if not room: raise HTTPException(404, "Sala não encontrada.")
    db.delete(room); db.commit()


@app.post("/api/v1/readings", response_model=ReadingOut, status_code=201)
def create_reading(payload: ReadingCreate, db: Session = Depends(get_db)):
    room = db.get(Room, payload.room_id)
    if not room: raise HTTPException(404, "Sala não encontrada.")
    reading = Reading(**payload.model_dump(), status=classify_consumption(payload.kwh, room.expected_kwh))
    db.add(reading); db.flush()
    alert = build_alert(reading, room)
    if alert: db.add(alert)
    db.commit(); db.refresh(reading); return reading


@app.get("/api/v1/readings", response_model=list[ReadingOut])
def list_readings(room_id: int | None = None, start: date | None = None, end: date | None = None, db: Session = Depends(get_db)):
    query = select(Reading).order_by(Reading.recorded_on.desc(), Reading.id.desc())
    if room_id: query = query.where(Reading.room_id == room_id)
    if start: query = query.where(Reading.recorded_on >= start)
    if end: query = query.where(Reading.recorded_on <= end)
    return db.scalars(query).all()


@app.get("/api/v1/alerts", response_model=list[AlertOut])
def list_alerts(db: Session = Depends(get_db)):
    return db.scalars(select(Alert).order_by(Alert.created_at.desc())).all()


@app.get("/api/v1/alerts/{alert_id}", response_model=AlertOut)
def get_alert(alert_id: int, db: Session = Depends(get_db)):
    alert = db.get(Alert, alert_id)
    if not alert: raise HTTPException(404, "Alerta não encontrado.")
    return alert


@app.get("/api/v1/reports/summary", response_model=ReportOut)
def summary(start: date | None = Query(None), end: date | None = Query(None), db: Session = Depends(get_db)):
    readings = list_readings(start=start, end=end, db=db)
    rooms = {room.id: room for room in db.scalars(select(Room)).all()}
    by_room = defaultdict(lambda: {"kwh": 0.0, "expected": 0.0, "excess": 0.0})
    for reading in readings:
        room = rooms[reading.room_id]; item = by_room[room.name]
        item["kwh"] += reading.kwh; item["expected"] += room.expected_kwh
        item["excess"] += max(0, reading.kwh - room.expected_kwh)
    total = sum(r.kwh for r in readings); expected = sum(rooms[r.room_id].expected_kwh for r in readings)
    excess = sum(max(0, r.kwh - rooms[r.room_id].expected_kwh) for r in readings)
    return {"total_kwh": total, "expected_kwh": expected, "excessive_kwh": excess, "estimated_savings_kwh": excess, "excessive_readings": sum(r.status == "EXCESSIVO" for r in readings), "by_room": [{"room": n, **v} for n, v in by_room.items()]}
