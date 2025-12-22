from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class VisionEventBase(BaseModel):
    pen_id: str
    bird_id: Optional[str] = None
    type: str  # e.g., "abnormal_behavior", "sick", "aggression"
    confidence: Optional[float] = None
    image_url: Optional[str] = None


class VisionEventCreate(VisionEventBase):
    pass


class VisionEventUpdate(BaseModel):
    type: Optional[str] = None
    confidence: Optional[float] = None
    image_url: Optional[str] = None


class VisionEventOut(VisionEventBase):
    id: str
    timestamp: datetime

    class Config:
        from_attributes = True
