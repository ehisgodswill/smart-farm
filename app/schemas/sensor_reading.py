from datetime import datetime
from pydantic import BaseModel
from app.models.enums import SensorTypeEnum


class SensorReadingCreate(BaseModel):
    sensor_id: str
    pen_id: str
    value: float
    timestamp: datetime | None = None


class SensorReadingOut(BaseModel):
    id: str
    sensor_id: str
    pen_id: str
    sensor_type: SensorTypeEnum
    value: float
    timestamp: datetime

    class Config:
        from_attributes = True
