from app.models.device_command import DeviceCommand

def create_device_command(
    db,
    device_id: str,
    device_type,
    action,
    source: str,
    rule_id: str | None = None,
):
    command = DeviceCommand(
        device_id=device_id,
        device_type=device_type,
        action=action,
        source=source,
        rule_id=rule_id,
    )

    db.add(command)
    db.commit()
    db.refresh(command)

    return command
