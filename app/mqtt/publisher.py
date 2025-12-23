import json
import paho.mqtt.client as mqtt

from app.models.device_command import DeviceCommand

MQTT_BROKER = "localhost"
MQTT_PORT = 1883


client = mqtt.Client()


def connect():
    if not client.is_connected():
        client.connect(MQTT_BROKER, MQTT_PORT, 60)


def publish_device_command(command: DeviceCommand):
    """
    Publish a device command to the pen controller
    """
    connect()

    topic = f"devices/{command.pen_id}/{command.device_id}/command"

    payload = {
        "command_id": command.id,
        "device_id": command.device_id,
        "pen_id": command.pen_id,
        "action": command.action.value,
        "issued_at": command.issued_at.isoformat(),
        "source": command.source,
    }

    client.publish(topic, json.dumps(payload), qos=1)
