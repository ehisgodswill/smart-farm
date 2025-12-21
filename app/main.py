from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, birds, devices, farms, pens, rules, sensors, sensor_readings, vision_events
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
# WebSocket Connection Manager
# -------------------------------------------------
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except:
                pass

manager = ConnectionManager()

# -------------------------------------------------
# WebSocket Endpoint
# -------------------------------------------------
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Keep connection alive and receive messages
            data = await websocket.receive_text()
            # Echo back or handle the message
            await websocket.send_json({"message": f"Received: {data}"})
    except WebSocketDisconnect:
        manager.disconnect(websocket)


# -------------------------------------------------
# Routers
# -------------------------------------------------
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(birds.router, prefix="/api/birds", tags=["Birds"])
app.include_router(devices.router, prefix="/api/devices", tags=["Devices"])
app.include_router(farms.router, prefix="/api/farms", tags=["Farms"])
app.include_router(pens.router, prefix="/api/pens", tags=["Pens"])
app.include_router(sensors.router, prefix="/api/sensors", tags=["Sensors"])
app.include_router(sensor_readings.router, prefix="/api/sensor-readings", tags=["Sensor Readings"])
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
