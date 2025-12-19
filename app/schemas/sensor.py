from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from app.models.enums import SensorTypeEnum


class SensorBase(BaseModel):
    pen_id: str
    type: SensorTypeEnum
    device_id: Optional[str] = None


class SensorCreate(SensorBase):
    pass


class SensorUpdate(BaseModel):
    type: Optional[SensorTypeEnum] = None
    device_id: Optional[str] = None


class SensorOut(SensorBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True
