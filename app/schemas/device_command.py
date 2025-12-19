from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from app.models.enums import DeviceTypeEnum, ActionValueEnum, CommandStatusEnum


class DeviceCommandBase(BaseModel):
    device_id: str
    device_type: DeviceTypeEnum
    action: ActionValueEnum
    source: str  # e.g., "rule_engine", "admin", "system"
    rule_id: Optional[str] = None


class DeviceCommandCreate(DeviceCommandBase):
    pass


class DeviceCommandUpdate(BaseModel):
    status: Optional[CommandStatusEnum] = None
    executed_at: Optional[datetime] = None


class DeviceCommandOut(DeviceCommandBase):
    id: str
    status: CommandStatusEnum
    created_at: datetime
    executed_at: Optional[datetime] = None

    class Config:
        orm_mode = True
