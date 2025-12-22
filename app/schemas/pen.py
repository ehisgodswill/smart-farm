from datetime import datetime
from pydantic import BaseModel

class PenBase(BaseModel):
    name: str
    capacity: int | None = None
    module_id: str | None = None  # MCU identifier


class PenCreate(PenBase):
    farm_id: str


class PenUpdate(BaseModel):
    name: str | None = None
    capacity: int | None = None
    module_id: str | None = None


class PenOut(PenBase):
    id: str
    farm_id: str
    created_at: datetime

    class Config:
        from_attributes = True
