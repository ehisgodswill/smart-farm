from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class Bird(Base):
    __tablename__ = "birds"

    id = Column(String, primary_key=True)
    pen_id = Column(String, ForeignKey("pens.id"), nullable=False)
    tag_id = Column(String, unique=True, nullable=True)
    hatch_date = Column(Date, nullable=True)
    age_days = Column(Integer, nullable=True)
    health_score = Column(Float, nullable=True)
    status = Column(String, default="healthy")
    created_at = Column(DateTime, default=datetime.utcnow)
