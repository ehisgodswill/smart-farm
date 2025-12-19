from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from app.models.enums import DeviceTypeEnum, ActionValueEnum


class DeviceBase(BaseModel):
    pen_id: str
    type: DeviceTypeEnum
    state: ActionValueEnum = ActionValueEnum.OFF
    last_command_at: Optional[datetime] = None


class DeviceCreate(DeviceBase):
    pass


class DeviceUpdate(BaseModel):
    type: Optional[DeviceTypeEnum] = None
    state: Optional[ActionValueEnum] = None
    last_command_at: Optional[datetime] = None


class DeviceOut(DeviceBase):
    id: str

    class Config:
        orm_mode = True
