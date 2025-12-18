import json
import uuid
from app.database import SessionLocal
from app.models.environment import EnvironmentReading
from app.services.automation import handle_temperature

DEVICE_MAP = {
    "A1": "esp32-sim-01"
}

def on_message(client, userdata, msg):
    if "environment" in msg.topic:
        payload = json.loads(msg.payload.decode())
        pen_id = payload["pen_id"]
        temperature = payload["temperature"]

        db = SessionLocal()
        reading = EnvironmentReading(
            id=str(uuid.uuid4()),
            pen_id=pen_id,
            temperature=temperature,
            humidity=payload["humidity"]
        )
        db.add(reading)
        db.commit()
        db.close()

        handle_temperature(
            pen_id=pen_id,
            device_id=DEVICE_MAP[pen_id],
            temperature=temperature
        )
