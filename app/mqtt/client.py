import json
import threading
import paho.mqtt.client as mqtt
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.sensor_service import create_sensor_reading
from app.services.rule_engine_service import evaluate_rules_for_reading

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "poultry/sensors/#"

client: mqtt.Client | None = None


def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    try:
        data = json.loads(payload)
        """
        Expected payload:
        {
            "sensor_id": "uuid",
            "pen_id": "uuid",
            "value": 23.5,
            "timestamp": "2025-12-19T07:00:00"
        }
        """
        db: Session = SessionLocal()
        reading = create_sensor_reading(
            db,
            sensor_id=data["sensor_id"],
            pen_id=data["pen_id"],
            value=float(data["value"]),
            timestamp=data.get("timestamp")
        )
        evaluate_rules_for_reading(db, reading)
        db.commit()
        db.close()
    except Exception as e:
        print(f"Error processing MQTT message: {e}")


def start_mqtt():
    global client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    thread = threading.Thread(target=client.loop_forever, daemon=True)
    thread.start()
