import json
import uuid
from app.database import SessionLocal
from app.models.environment import EnvironmentReading
from app.services.rule_engine import evaluate_rules

def on_message(client, userdata, msg):
    if "environment" in msg.topic:
        payload = json.loads(msg.payload.decode())
        pen_id = payload["pen_id"]
        temperature = payload["temperature"]
        humidity = payload["humidity"]

        # Save reading
        db = SessionLocal()
        reading = EnvironmentReading(
            id=str(uuid.uuid4()),
            pen_id=pen_id,
            temperature=temperature,
            humidity=humidity
        )
        db.add(reading)
        db.commit()
        db.close()

        # Evaluate rules for temperature and humidity
        evaluate_rules(pen_id, "temperature", temperature)
        evaluate_rules(pen_id, "humidity", humidity)
