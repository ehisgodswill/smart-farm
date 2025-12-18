import paho.mqtt.client as mqtt
import json

mqtt_client = mqtt.Client()

def start_mqtt():
    mqtt_client.connect("localhost", 1883)
    mqtt_client.loop_start()

def send_device_command(device_id, pen_id, device, action):
    payload = {
        "device_id": device_id,
        "pen_id": pen_id,
        "device": device,
        "action": action
    }
    mqtt_client.publish(
        f"farm/device/{device_id}/command",
        json.dumps(payload)
    )
