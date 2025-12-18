from sqlalchemy import Column, String, DateTime
from app.database import Base
import uuid
from datetime import datetime

class Bird(Base):
    __tablename__ = "birds"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    pen_id = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
