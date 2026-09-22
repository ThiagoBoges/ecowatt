from .models import Alert, Reading, Room


def classify_consumption(kwh: float, expected_kwh: float) -> str:
    return "EXCESSIVO" if kwh > expected_kwh else "NORMAL"


def build_alert(reading: Reading, room: Room) -> Alert | None:
    if reading.status != "EXCESSIVO":
        return None
    excess = reading.kwh - room.expected_kwh
    return Alert(
        reading_id=reading.id,
        message=(f"{room.name}: consumo de {reading.kwh:.2f} kWh excedeu o esperado "
                 f"de {room.expected_kwh:.2f} kWh em {excess:.2f} kWh."),
    )

