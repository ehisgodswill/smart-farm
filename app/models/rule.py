from sqlalchemy import Column, String, Boolean, DateTime, Float
from app.database import Base
from datetime import datetime
import uuid

class Rule(Base):
    __tablename__ = "rules"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    # null = global rule
    pen_id = Column(String, nullable=True)
    # Rule logic (engine-friendly)
    condition = Column(String, nullable=False)  # e.g. "temperature > 30"
    action = Column(String, nullable=False)     # e.g. "fan:ON"
    enabled = Column(Boolean, default=True)
    priority = Column(Float, default=1.0)
    created_at = Column(DateTime, default=datetime.utcnow)
