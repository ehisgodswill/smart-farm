from datetime import datetime
from pydantic import BaseModel

class PenBase(BaseModel):
    farm_id: str
    name: str
    capacity: int | None = None


class PenCreate(PenBase):
    pass


class PenUpdate(BaseModel):
    name: str | None = None
    capacity: int | None = None


class PenOut(PenBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True
