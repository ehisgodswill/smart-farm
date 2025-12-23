from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Any

class VisionEventCreate(BaseModel):
    farm_id: str
    pen_id: str
    event: str
    severity: str
    confidence: float = Field(ge=0.0, le=1.0)  # Between 0 and 1
    details: dict[str, Any] = {}
    timestamp: str | None = None
    
    @field_validator('timestamp')
    @classmethod
    def parse_timestamp(cls, v: str | None) -> str | None:
        if v:
            return v.replace("Z", "+00:00")
        return v

class VisionEventOut(BaseModel):
    id: str
    farm_id: str
    pen_id: str
    event: str
    severity: str
    confidence: float
    details: str  # JSON string in response
    created_at: datetime

    class Config:
        from_attributes = True