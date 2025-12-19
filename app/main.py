from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import birds, sensors, devices, vision, alerts, rules
from app.mqtt.client import start_mqtt
from app.database import Base, engine

app = FastAPI(title="Smart Poultry Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev server
    ],
    allow_credentials=True,
    allow_methods=["*"],        # GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],        # Content-Type, Authorization, etc.
)

# Create tables automatically
Base.metadata.create_all(bind=engine)

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
