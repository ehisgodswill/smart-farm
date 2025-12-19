import json
import paho.mqtt.client as mqtt
from app.database import SessionLocal
from app.services.sensor_ingestion_service import ingest_sensor_reading

MQTT_BROKER = "localhost"
MQTT_TOPIC = "sensors/+/readings"

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())

    db = SessionLocal()
    try:
        ingest_sensor_reading(db, payload)
    finally:
        db.close()

def start_mqtt():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(MQTT_BROKER)
    client.subscribe(MQTT_TOPIC)
    client.loop_start()
