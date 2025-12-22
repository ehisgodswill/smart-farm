from datetime import datetime
from pydantic import BaseModel
from app.models.enums import ActionValueEnum


class DeviceCommandCreate(BaseModel):
    action: ActionValueEnum
    source: str = "manual"


class DeviceCommandOut(BaseModel):
    id: str
    device_id: str
    pen_id: str
    action: ActionValueEnum
    source: str
    issued_at: datetime

    class Config:
        from_attributes = True
