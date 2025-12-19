from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RuleCreate(BaseModel):
    name: str
    pen_id: str
    condition: str
    action: str
    enabled: Optional[bool] = True
    priority: float = 1.0

class RuleRead(BaseModel):
    id: str
    name: str
    pen_id: str
    condition: str
    action: str
    enabled: bool
    created_at: datetime

    class Config:
        orm_mode = True  # Needed to convert SQLAlchemy objects to Pydantic
