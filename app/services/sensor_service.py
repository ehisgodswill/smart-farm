import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.sensor import Sensor

def get_sensor(db: Session, sensor_id: str) -> Sensor | None:
    return db.query(Sensor).filter(Sensor.id == sensor_id).first()

def get_sensors(db: Session, skip: int = 0, limit: int = 100) -> list[Sensor]:
    return db.query(Sensor).offset(skip).limit(limit).all()

def create_sensor(
    db: Session,
    pen_id: str,
    type: str,
    device_id: str | None = None,
    id: str | None = None
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
