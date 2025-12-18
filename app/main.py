from fastapi import FastAPI
from app.api import birds, sensors, devices, vision, alerts, rules
from app.mqtt.client import start_mqtt

app = FastAPI(title="Smart Poultry Server")

app.include_router(birds.router, prefix="/api/birds")
# app.include_router(sensors.router, prefix="/api/sensors")
# app.include_router(devices.router, prefix="/api/devices")
# app.include_router(vision.router, prefix="/api/vision")
# app.include_router(alerts.router, prefix="/api/alerts")
app.include_router(rules.router, prefix="/api/rules")

@app.on_event("startup")
def startup():
    start_mqtt()

@app.get("/")
def health():
    return {"status": "server running"}
