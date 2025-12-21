import time
import random
import requests
from datetime import datetime, timezone

API_BASE = "http://localhost:8000/api"
PEN_ID = "pen-001"
TEMP_SENSOR_ID = "temp-sensor-001"
HUM_SENSOR_ID = "hum-sensor-001"

def send_reading(sensor_id: str, value: float):
    payload = {
        "sensor_id": sensor_id,
        "pen_id": PEN_ID,
        "value": value,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    r = requests.post(f"{API_BASE}/sensor-readings", json=payload)
    r.raise_for_status()

    print(f"Sent {sensor_id}: {value}")

if __name__ == "__main__":
    print("Starting pen simulation...")

    while True:
        temp = round(random.uniform(28.0, 36.0), 2)
        hum = round(random.uniform(55.0, 80.0), 2)

        send_reading(TEMP_SENSOR_ID, temp)
        send_reading(HUM_SENSOR_ID, hum)

        time.sleep(2)
