from datetime import date
from pydantic import BaseModel
from typing import Optional


class BirdBase(BaseModel):
    pen_id: str
    tag_id: Optional[str] = None
    hatch_date: Optional[date] = None
    age_days: Optional[int] = None
    health_score: Optional[float] = None
    status: str = "healthy"


class BirdCreate(BirdBase):
    pass


class BirdUpdate(BaseModel):
    tag_id: Optional[str] = None
    hatch_date: Optional[date] = None
    age_days: Optional[int] = None
    health_score: Optional[float] = None
    status: Optional[str] = None


class BirdOut(BirdBase):
    id: str

    class Config:
        orm_mode = True
