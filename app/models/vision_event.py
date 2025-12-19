from sqlalchemy import Column, DateTime, Float, ForeignKey, String
from datetime import datetime
from app.database import Base

class VisionEvent(Base):
    __tablename__ = "vision_events"

    id = Column(String, primary_key=True)
    pen_id = Column(String, ForeignKey("pens.id"))
    bird_id = Column(String, ForeignKey("birds.id"), nullable=True)
    type = Column(String, nullable=False)  # abnormal_behavior, sick, aggression
    confidence = Column(Float, nullable=True)
    image_url = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
