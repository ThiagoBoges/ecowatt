from datetime import date, datetime

from sqlalchemy import Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Room(Base):
    __tablename__ = "rooms"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    sector: Mapped[str] = mapped_column(String(100))
    responsible: Mapped[str] = mapped_column(String(100))
    expected_kwh: Mapped[float] = mapped_column(Float)
    readings: Mapped[list["Reading"]] = relationship(back_populates="room", cascade="all, delete-orphan")


class Reading(Base):
    __tablename__ = "readings"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"), index=True)
    recorded_on: Mapped[date] = mapped_column(Date, index=True)
    kwh: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(12))
    room: Mapped[Room] = relationship(back_populates="readings")
    alert: Mapped["Alert | None"] = relationship(back_populates="reading", cascade="all, delete-orphan", uselist=False)


class Alert(Base):
    __tablename__ = "alerts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    reading_id: Mapped[int] = mapped_column(ForeignKey("readings.id"), unique=True)
    message: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    reading: Mapped[Reading] = relationship(back_populates="alert")

