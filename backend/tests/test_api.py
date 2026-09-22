import os
os.environ["DATABASE_URL"] = "sqlite:///./test_ecowatt.db"

from fastapi.testclient import TestClient
from app.database import Base, engine
from app.main import app

client = TestClient(app)


def setup_module():
    Base.metadata.drop_all(engine); Base.metadata.create_all(engine)


def test_room_crud_and_excessive_alert():
    room = client.post("/api/v1/rooms", json={"name":"Sala 101","sector":"Bloco A","responsible":"Coordenação","expected_kwh":5}).json()
    assert room["id"]
    reading = client.post("/api/v1/readings", json={"room_id":room["id"],"recorded_on":"2026-09-22","kwh":12}).json()
    assert reading["status"] == "EXCESSIVO"
    assert len(client.get("/api/v1/alerts").json()) == 1
    report = client.get("/api/v1/reports/summary").json()
    assert report["estimated_savings_kwh"] == 7


def test_normal_reading_has_no_alert():
    room = client.post("/api/v1/rooms", json={"name":"Laboratório","sector":"Bloco B","responsible":"TI","expected_kwh":8}).json()
    response = client.post("/api/v1/readings", json={"room_id":room["id"],"recorded_on":"2026-09-21","kwh":8})
    assert response.status_code == 201
    assert response.json()["status"] == "NORMAL"


def test_rejects_invalid_consumption():
    assert client.post("/api/v1/readings", json={"room_id":1,"recorded_on":"2026-09-21","kwh":0}).status_code == 422


def test_filters_readings_by_room_and_period():
    room = client.get("/api/v1/rooms").json()[0]
    response = client.get(f"/api/v1/readings?room_id={room['id']}&start=2026-09-22&end=2026-09-22")
    assert response.status_code == 200
    assert all(item["room_id"] == room["id"] for item in response.json())


def test_get_alert_and_update_room():
    alert = client.get("/api/v1/alerts").json()[0]
    assert client.get(f"/api/v1/alerts/{alert['id']}").status_code == 200
    room = client.get("/api/v1/rooms").json()[0]
    response = client.put(f"/api/v1/rooms/{room['id']}", json={"name":room["name"],"sector":"Bloco Atualizado","responsible":"Coordenação","expected_kwh":6})
    assert response.json()["expected_kwh"] == 6
