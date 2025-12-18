import json
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

DEVICE_ID = "esp32-sim-01"

DEVICE_STATES = {
    "fan": "OFF",
    "heater": "OFF",
    "feeder": "OFF",
    "light": "OFF"
}

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())

    device = payload["device"]
    action = payload["action"]

    DEVICE_STATES[device] = action

    print(f"[DEVICE] {device} set to {action}")

    status_payload = {
        "device_id": DEVICE_ID,
        "device": device,
        "status": action,
        "timestamp": datetime.utcnow().isoformat()
    }

    client.publish(
        f"farm/device/{DEVICE_ID}/status",
        json.dumps(status_payload)
    )

client = mqtt.Client(client_id=DEVICE_ID)
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe(f"farm/device/{DEVICE_ID}/command")
client.loop_forever()
