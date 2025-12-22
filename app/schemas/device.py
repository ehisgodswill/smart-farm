from datetime import datetime
from pydantic import BaseModel
from app.models.enums import DeviceTypeEnum, ActionValueEnum


class DeviceCreate(BaseModel):
    pen_id: str
    type: DeviceTypeEnum


class DeviceUpdate(BaseModel):
    state: ActionValueEnum | None = None


class DeviceOut(BaseModel):
    id: str
    pen_id: str
    type: DeviceTypeEnum
    state: ActionValueEnum
    last_command_at: datetime | None

    class Config:
        from_attributes = True
