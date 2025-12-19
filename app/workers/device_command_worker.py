from datetime import datetime
from time import sleep
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.device_command import DeviceCommand
from app.workers.mqtt_dispatcher import send_device_command
from app.models.enums import CommandStatusEnum

POLL_INTERVAL = 2  # seconds

def run_device_command_worker():
    db: Session = SessionLocal()

    while True:
        commands = (
            db.query(DeviceCommand)
            .filter(DeviceCommand.status == CommandStatusEnum.pending)
            .limit(10)
            .all()
        )

        for command in commands:
            try:
                send_device_command(command)
                command.status = CommandStatusEnum.sent
                command.executed_at = datetime.utcnow()

                db.commit()

            except Exception as e:
                command.status = CommandStatusEnum.failed
                db.commit()

        sleep(POLL_INTERVAL)
