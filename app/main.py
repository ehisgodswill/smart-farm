from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import birds, devices, pens, rules, sensors, sensor_readings, vision_events
from app.mqtt.client import start_mqtt

app = FastAPI(
    title="Smart Poultry Server",
    version="1.0.0"
)

# -------------------------------------------------
# CORS
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Frontend (Vite)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# Routers
# -------------------------------------------------
app.include_router(birds.router, prefix="/api/birds", tags=["Birds"])
app.include_router(devices.router, prefix="/api/devices", tags=["Devices"])
app.include_router(pens.router, prefix="/api/pens", tags=["Pens"])
app.include_router(sensors.router, prefix="/api/sensors", tags=["Sensors"])
app.include_router(sensor_readings.router, prefix="/api/sensor-readings", tags=["Sensor-Readings"])
app.include_router(rules.router, prefix="/api/rules", tags=["Rules"])
app.include_router(vision_events.router, prefix="/api/vision-events", tags=["Vision"])

# -------------------------------------------------
# Startup / Shutdown
# -------------------------------------------------
@app.on_event("startup")
def on_startup():
    """
    Start background services (MQTT, schedulers, etc.)
    """
    start_mqtt()

@app.on_event("shutdown")
def on_shutdown():
    """
    Graceful shutdown hooks (optional)
    """
    pass

# -------------------------------------------------
# Health Check
# -------------------------------------------------
@app.get("/", tags=["Health"])
def health():
    return {"status": "server running"}
