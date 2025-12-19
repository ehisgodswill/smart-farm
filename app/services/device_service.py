import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.device import Device
from app.models.enums import ActionValueEnum


def get_device(db: Session, device_id: str) -> Device | None:
    return db.query(Device).filter(Device.id == device_id).first()


def get_devices(db: Session, skip: int = 0, limit: int = 100) -> list[Device]:
    return db.query(Device).offset(skip).limit(limit).all()


def create_device(
    db: Session,
    pen_id: str,
    type: str,
    state: ActionValueEnum = ActionValueEnum.OFF,
    last_command_at: datetime | None = None,
    id: str | None = None
) -> Device:
    device = Device(
        id=id or str(uuid.uuid4()),
        pen_id=pen_id,
        type=type,
        state=state,
        last_command_at=last_command_at
    )
    db.add(device)
    db.commit()
    db.refresh(device)
    return device


def update_device(
    db: Session,
    device_id: str,
    **kwargs
) -> Device | None:
    device = get_device(db, device_id)
    if not device:
        return None
    for key, value in kwargs.items():
        if value is not None and hasattr(device, key):
            setattr(device, key, value)
    db.commit()
    db.refresh(device)
    return device


def delete_device(db: Session, device_id: str) -> Device | None:
    device = get_device(db, device_id)
    if not device:
        return None
    db.delete(device)
    db.commit()
    return device
