import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from app.models.device import Device
from app.models.enums import ActionValueEnum, DeviceTypeEnum


def get_device(db: Session, device_id: str) -> Device | None:
    return db.query(Device).filter(Device.id == device_id).first()


def get_devices(
    db: Session,
    skip: int = 0,
    limit: int = 100
) -> list[Device]:
    return (
        db.query(Device)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_device(
    db: Session,
    pen_id: str,
    type: DeviceTypeEnum,
    id: str | None = None
) -> Device:
    device = Device(
        id=id or str(uuid.uuid4()),
        pen_id=pen_id,
        type=type,
        state=ActionValueEnum.OFF,
        last_command_at=None
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

    state_changed = False

    for key, value in kwargs.items():
        if value is not None and hasattr(device, key):
            setattr(device, key, value)
            if key == "state":
                state_changed = True

    if state_changed:
        device.last_command_at = datetime.now(timezone.utc)

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
