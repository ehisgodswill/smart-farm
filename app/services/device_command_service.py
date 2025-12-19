import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.device_command import DeviceCommand
from app.models.enums import CommandStatusEnum


def get_device_command(db: Session, command_id: str) -> DeviceCommand | None:
    return db.query(DeviceCommand).filter(DeviceCommand.id == command_id).first()


def get_device_commands(db: Session, skip: int = 0, limit: int = 100) -> list[DeviceCommand]:
    return db.query(DeviceCommand).offset(skip).limit(limit).all()


def create_device_command(
    db: Session,
    device_id: str,
    device_type: str,
    action: str,
    source: str,
    rule_id: str | None = None,
    id: str | None = None
) -> DeviceCommand:
    cmd = DeviceCommand(
        id=id or str(uuid.uuid4()),
        device_id=device_id,
        device_type=device_type,
        action=action,
        source=source,
        rule_id=rule_id,
        status=CommandStatusEnum.pending
    )
    db.add(cmd)
    db.commit()
    db.refresh(cmd)
    return cmd


def update_device_command(
    db: Session,
    command_id: str,
    **kwargs
) -> DeviceCommand | None:
    cmd = get_device_command(db, command_id)
    if not cmd:
        return None
    for key, value in kwargs.items():
        if value is not None and hasattr(cmd, key):
            setattr(cmd, key, value)
    db.commit()
    db.refresh(cmd)
    return cmd


def delete_device_command(db: Session, command_id: str) -> DeviceCommand | None:
    cmd = get_device_command(db, command_id)
    if not cmd:
        return None
    db.delete(cmd)
    db.commit()
    return cmd
