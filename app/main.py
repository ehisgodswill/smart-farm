from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import birds, sensors, devices, vision, alerts, rules
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
app.include_router(rules.router, prefix="/api/rules", tags=["Rules"])

# Uncomment as modules are ready
# app.include_router(sensors.router, prefix="/api/sensors", tags=["Sensors"])
# app.include_router(devices.router, prefix="/api/devices", tags=["Devices"])
# app.include_router(vision.router, prefix="/api/vision", tags=["Vision"])
# app.include_router(alerts.router, prefix="/api/alerts", tags=["Alerts"])

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
