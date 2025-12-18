from app.mqtt.client import send_device_command

MAX_TEMP = 30.0

def handle_temperature(pen_id, device_id, temperature):
    if temperature > MAX_TEMP:
        send_device_command(device_id, pen_id, "fan", "ON")
    else:
        send_device_command(device_id, pen_id, "fan", "OFF")
