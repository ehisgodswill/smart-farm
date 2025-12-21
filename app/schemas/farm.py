from datetime import datetime
from pydantic import BaseModel, Field


class FarmBase(BaseModel):
    name: str = Field(..., min_length=1)
    location: str | None = None


class FarmCreate(FarmBase):
    pass


class FarmUpdate(BaseModel):
    name: str | None = None
    location: str | None = None


class FarmOut(FarmBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True
