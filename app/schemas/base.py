from datetime import datetime
from pydantic import BaseModel

class BaseSchema(BaseModel):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True  # Pydantic v2 (orm_mode replacement)
