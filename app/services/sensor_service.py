import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.sensor import Sensor
from app.models.sensor_reading import SensorReading
from app.services.rule_engine_service import evaluate_rules_for_sensor

def get_sensor(db: Session, sensor_id: str) -> Sensor | None:
    return db.query(Sensor).filter(Sensor.id == sensor_id).first()

def get_sensors_by_pen(db: Session, pen_id: str):
    return db.query(Sensor).filter(Sensor.pen_id == pen_id).all()

def create_sensor(
    db: Session,
    pen_id: str,
    type: str,
    device_id: str | None = None,
) -> Sensor:
    sensor = Sensor(
        id=id or str(uuid.uuid4()),
        pen_id=pen_id,
        type=type,
        device_id=device_id
    )
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor

def update_sensor(
    db: Session,
    sensor_id: str,
    **kwargs
) -> Sensor | None:
    sensor = get_sensor(db, sensor_id)
    if not sensor:
        return None
    for key, value in kwargs.items():
        if value is not None and hasattr(sensor, key):
            setattr(sensor, key, value)
    db.commit()
    db.refresh(sensor)
    return sensor

def delete_sensor(db: Session, sensor_id: str) -> Sensor | None:
    sensor = get_sensor(db, sensor_id)
    if not sensor:
        return None
    db.delete(sensor)
    db.commit()
    return sensor

def create_sensor_reading(
    db: Session,
    sensor_id: str,
    pen_id: str,
    value: float,
    timestamp: datetime | None = None
) -> SensorReading:
    """
    Create a sensor reading and trigger the rule engine.
    """
    sensor: Sensor | None = db.query(Sensor).filter(Sensor.id == sensor_id).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not registered")

    reading = SensorReading(
        sensor_id=sensor.id,
        pen_id=pen_id,
        sensor_type=sensor.type,
        value=value,
        timestamp=timestamp or datetime.now(timezone.utc)
    )

    db.add(reading)
    db.commit()
    db.refresh(reading)

    # Trigger rule engine AFTER commit
    evaluate_rules_for_sensor(db, reading)

    return reading
