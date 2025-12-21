from sqlalchemy.orm import Session
from datetime import datetime, timezone
from fastapi import HTTPException

from app.models.sensor import Sensor
from app.models.sensor_reading import SensorReading
from app.services.rule_engine_service import evaluate_rules_for_sensor


def ingest_sensor_reading(db: Session, payload: dict) -> SensorReading:
    sensor = db.get(Sensor, payload["sensor_id"])
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not registered")

    reading = SensorReading(
        sensor_id=sensor.id,
        pen_id=payload["pen_id"],
        sensor_type=sensor.type,
        value=payload["value"],
        timestamp=payload.get("timestamp")
        or datetime.now(timezone.utc),
    )

    db.add(reading)
    db.commit()
    db.refresh(reading)

    # Fire rule engine AFTER persistence
    evaluate_rules_for_sensor(db, reading)

    return reading

def get_sensor_readings(
    db: Session,
    pen_id: str,
    sensor_type: str | None = None,
    limit: int = 100,
):
    q = (
        db.query(SensorReading)
        .filter(SensorReading.pen_id == pen_id)
        .order_by(SensorReading.timestamp.desc())
        .limit(limit)
    )

    if sensor_type:
        q = q.filter(SensorReading.sensor_type == sensor_type)

    return q.all()


def get_sensor_reading(db: Session, reading_id: str):
    return db.get(SensorReading, reading_id)
