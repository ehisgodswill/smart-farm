from sqlalchemy import Column, Float, String, DateTime
from datetime import datetime
from app.database import Base

class EnvironmentReading(Base):
    __tablename__ = "environment_readings"

    id = Column(String, primary_key=True)
    pen_id = Column(String)
    temperature = Column(Float)
    humidity = Column(Float)
    recorded_at = Column(DateTime, default=datetime.utcnow)
