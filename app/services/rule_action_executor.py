from sqlalchemy.orm import Session
from app.models.rule import Rule
from app.models.sensor_reading import SensorReading
from app.services.device_command_service import issue_device_command
from app.models.device import Device

def execute_device_action(
    db: Session,
    rule: Rule,
    reading: SensorReading,
):
    """
    Translates a triggered rule into a device command.
    """

    # 1. Find target device
    device = (
        db.query(Device)
        .filter(
            Device.pen_id == reading.pen_id,
            Device.type == rule.action_device,
            Device.active == True,
        )
        .first()
    )

    if not device:
        return None

    # 2. Create command (DO NOT EXECUTE HERE)
    command = issue_device_command(
        db=db,
        device_id=device.id,
        action=rule.action_value,
        source="rule_engine",
    )

    return command
