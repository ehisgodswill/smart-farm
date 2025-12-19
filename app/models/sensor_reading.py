from sqlalchemy import Column, DateTime, Float, ForeignKey, String
from datetime import datetime
from app.database import Base

class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id = Column(String, primary_key=True)
    sensor_id = Column(String, ForeignKey("sensors.id"), nullable=False)
    pen_id = Column(String, ForeignKey("pens.id"), nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
