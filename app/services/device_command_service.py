from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.models.device import Device
from app.models.device_command import DeviceCommand
from app.models.enums import ActionValueEnum
from app.mqtt.publisher import publish_device_command


def issue_device_command(
    db: Session,
    device_id: str,
    action: ActionValueEnum,
    source: str
) -> DeviceCommand:
    device = db.query(Device).filter(Device.id == device_id).first()
    if not device:
        raise ValueError("Device not found")

    command = DeviceCommand(
        device_id=device.id,
        pen_id=device.pen_id,
        action=action,
        source=source,
        issued_at=datetime.now(timezone.utc)
    )

    # 1️⃣ Persist command
    db.add(command)

    # 2️⃣ Update device state optimistically
    device.state = action
    device.last_command_at = command.issued_at

    db.commit()
    db.refresh(command)

    # 3️⃣ Publish to MQTT AFTER commit
    publish_device_command(command)

    return command
