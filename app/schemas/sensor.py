from datetime import datetime
from pydantic import BaseModel
from app.models.enums import SensorTypeEnum

class SensorBase(BaseModel):
    type: SensorTypeEnum
    device_id: str | None = None  # MCU channel

class SensorCreate(SensorBase):
    pen_id: str

class SensorUpdate(BaseModel):
    device_id: str | None = None

class SensorOut(SensorBase):
    id: str
    pen_id: str
    created_at: datetime

    class Config:
        from_attributes = True
