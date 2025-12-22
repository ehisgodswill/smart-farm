import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from app.models.device import Device
from app.models.enums import ActionValueEnum


def get_device(db: Session, device_id: str) -> Device | None:
    return db.query(Device).filter(Device.id == device_id).first()


def get_devices_by_pen(
    db: Session,
    pen_id: str
) -> list[Device]:
    return (
        db.query(Device)
        .filter(Device.pen_id == pen_id)
        .order_by(Device.last_command_at.desc().nullslast())
        .all()
    )


def create_device(
    db: Session,
    pen_id: str,
    type: str
) -> Device:
    device = Device(
        id=str(uuid.uuid4()),
        pen_id=pen_id,
        type=type,
        state=ActionValueEnum.OFF
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


def delete_device(
    db: Session,
    device_id: str
) -> Device | None:
    device = get_device(db, device_id)
    if not device:
        return None

    db.delete(device)
    db.commit()
    return device
