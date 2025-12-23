import json
import paho.mqtt.client as mqtt
from sqlalchemy.orm import Session

from app.utils.db import SessionLocal
from app.mqtt.vision_handler import handle_vision_message

MQTT_BROKER = "localhost"
MQTT_PORT = 1883

VISION_TOPICS = [
    ("vision/+/+/metrics", 1),
    ("vision/+/+/events", 1),
    ("vision/+/health", 1),
]


def on_connect(client, userdata, flags, rc):
    print("MQTT connected with code", rc)
    for topic, qos in VISION_TOPICS:
        client.subscribe(topic, qos)


def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
    except Exception:
        print("Invalid JSON payload")
        return

    db: Session = SessionLocal()
    try:
        handle_vision_message(db, msg.topic, payload)
    finally:
        db.close()


def start_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
