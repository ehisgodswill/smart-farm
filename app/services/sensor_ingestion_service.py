from sqlalchemy.orm import Session
from datetime import datetime
from app.models.sensor import Sensor
from app.models.sensor_reading import SensorReading
from app.services.rule_engine import evaluate_rules_for_sensor
from fastapi import HTTPException

def ingest_sensor_reading(db: Session, payload: dict) -> SensorReading:
    sensor = db.query(Sensor).filter(Sensor.id == payload["sensor_id"]).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not registered")

    reading = SensorReading(
        sensor_id=sensor.id,
        pen_id=payload["pen_id"],
        value=payload["value"],
        timestamp=payload.get("timestamp", datetime.utcnow())
    )

    db.add(reading)
    db.commit()
    db.refresh(reading)

    # Trigger rule engine AFTER commit
    evaluate_rules_for_sensor(db, reading)

    return reading
