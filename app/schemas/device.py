from datetime import datetime
from pydantic import BaseModel
from app.models.enums import DeviceTypeEnum, ActionValueEnum

class DeviceBase(BaseModel):
    type: DeviceTypeEnum

class DeviceCreate(DeviceBase):
    pen_id: str

class DeviceUpdate(BaseModel):
    state: ActionValueEnum | None = None

class DeviceOut(DeviceBase):
    id: str
    pen_id: str
    state: ActionValueEnum
    last_command_at: datetime | None

    class Config:
        from_attributes = True
