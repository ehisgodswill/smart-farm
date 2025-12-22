from datetime import datetime
from pydantic import BaseModel

class SensorReadingCreate(BaseModel):
    sensor_id: str
    pen_id: str
    value: float

class SensorReadingOut(BaseModel):
    id: str
    sensor_id: str
    pen_id: str
    value: float
    timestamp: datetime

    class Config:
        from_attributes = True
