import json
import paho.mqtt.publish as publish

MQTT_HOST = "localhost"
MQTT_PORT = 1883

def send_device_command(command):
    topic = f"devices/{command.device_id}/commands"

    payload = {
        "device_id": command.device_id,
        "device_type": command.device_type.value,
        "action": command.action.value,
        "command_id": command.id,
    }

    publish.single(
        topic,
        json.dumps(payload),
        hostname=MQTT_HOST,
        port=MQTT_PORT,
    )
