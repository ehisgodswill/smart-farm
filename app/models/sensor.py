from sqlalchemy import Column, DateTime, Enum as SQLEnum, ForeignKey, String
from datetime import datetime
from app.database import Base
from app.models.enums import SensorTypeEnum

class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(String, primary_key=True)
    pen_id = Column(String, ForeignKey("pens.id"), nullable=False)
    type = Column(SQLEnum(SensorTypeEnum), nullable=False)
    device_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
