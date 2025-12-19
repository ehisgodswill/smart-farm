from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from .base import BaseSchema

# ---------- REQUEST SCHEMAS ----------

class BirdCreate(BaseModel):
    tag_id: str = Field(..., min_length=3, max_length=50)
    breed: Optional[str] = None
    hatch_date: Optional[datetime] = None

class BirdUpdate(BaseModel):
    breed: Optional[str] = None
    is_active: Optional[bool] = None

# ---------- RESPONSE SCHEMA ----------

class BirdOut(BaseSchema):
    tag_id: str
    breed: Optional[str] = None
    hatch_date: Optional[datetime] = None
    is_active: bool
