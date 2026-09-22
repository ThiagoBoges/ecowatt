from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


class RoomBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    sector: str = Field(min_length=2, max_length=100)
    responsible: str = Field(min_length=2, max_length=100)
    expected_kwh: float = Field(gt=0)


class RoomCreate(RoomBase): pass
class RoomUpdate(RoomBase): pass
class RoomOut(RoomBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ReadingCreate(BaseModel):
    room_id: int
    recorded_on: date
    kwh: float = Field(gt=0)


class ReadingOut(BaseModel):
    id: int
    room_id: int
    recorded_on: date
    kwh: float
    status: str
    model_config = ConfigDict(from_attributes=True)


class AlertOut(BaseModel):
    id: int
    reading_id: int
    message: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class ReportOut(BaseModel):
    total_kwh: float
    expected_kwh: float
    excessive_kwh: float
    estimated_savings_kwh: float
    excessive_readings: int
    by_room: list[dict]

