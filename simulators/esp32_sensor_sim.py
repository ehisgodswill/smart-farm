import time
import json
import random
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

DEVICE_ID = "esp32-sim-01"
PEN_ID = "A1"

client = mqtt.Client(client_id=DEVICE_ID)
client.connect(BROKER, PORT, keepalive=60)

def generate_environment():
    return {
        "device_id": DEVICE_ID,
        "pen_id": PEN_ID,
        "temperature": round(random.uniform(26.0, 34.0), 2),
        "humidity": round(random.uniform(50.0, 75.0), 2),
        "timestamp": datetime.utcnow().isoformat()
    }

def generate_water():
    return {
        "device_id": DEVICE_ID,
        "pen_id": PEN_ID,
        "flow_rate": round(random.uniform(0.5, 1.5), 2),
        "timestamp": datetime.utcnow().isoformat()
    }

while True:
    env_payload = generate_environment()
    water_payload = generate_water()

    client.publish(
        f"farm/pen/{PEN_ID}/environment",
        json.dumps(env_payload)
    )

    client.publish(
        f"farm/pen/{PEN_ID}/water",
        json.dumps(water_payload)
    )

    print("Published:", env_payload)

    time.sleep(5)
