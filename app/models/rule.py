from sqlalchemy import Column, Boolean, DateTime, Enum as SQLEnum, Float, ForeignKey, String
from datetime import datetime
from app.database import Base
from app.models.enums import SensorTypeEnum, DeviceTypeEnum, OperatorEnum, ActionValueEnum

class Rule(Base):
    __tablename__ = "rules"

    id = Column(String, primary_key=True)
    pen_id = Column(String, ForeignKey("pens.id"), nullable=True)  # null = global
    sensor_type = Column(SQLEnum(SensorTypeEnum), nullable=False)
    operator = Column(SQLEnum(OperatorEnum), nullable=False)
    threshold = Column(Float, nullable=False)
    action_device = Column(SQLEnum(DeviceTypeEnum), nullable=False)
    action_value = Column(SQLEnum(ActionValueEnum), nullable=False)
    priority = Column(Float, default=1.0)
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
