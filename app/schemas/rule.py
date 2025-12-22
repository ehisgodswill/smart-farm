from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from app.models.enums import SensorTypeEnum, DeviceTypeEnum, OperatorEnum, ActionValueEnum


class RuleBase(BaseModel):
    pen_id: Optional[str] = None  # null = global
    sensor_type: SensorTypeEnum
    operator: OperatorEnum
    threshold: float
    action_device: DeviceTypeEnum
    action_value: ActionValueEnum
    priority: Optional[int] = 1
    enabled: Optional[bool] = True


class RuleCreate(RuleBase):
    pass


class RuleUpdate(BaseModel):
    sensor_type: Optional[SensorTypeEnum] = None
    operator: Optional[OperatorEnum] = None
    threshold: Optional[float] = None
    action_device: Optional[DeviceTypeEnum] = None
    action_value: Optional[ActionValueEnum] = None
    priority: Optional[int] = None
    enabled: Optional[bool] = None
    pen_id: Optional[str] = None


class RuleOut(RuleBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True
