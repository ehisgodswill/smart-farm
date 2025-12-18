from sqlalchemy import Column, String, Float, Boolean, DateTime
from app.database import Base
from datetime import datetime
import uuid

class Rule(Base):
    __tablename__ = "rules"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    pen_id = Column(String, nullable=True)  # null = global
    sensor_type = Column(String, nullable=False)  # e.g., temperature, humidity
    operator = Column(String, nullable=False)     # >, <, >=, <=
    threshold = Column(Float, nullable=False)
    action_device = Column(String, nullable=False)  # fan, heater, feeder
    action_value = Column(String, nullable=False)   # ON/OFF, OPEN/CLOSE
    enabled = Column(Boolean, default=True)
    priority = Column(Float, default=1.0)
    created_at = Column(DateTime, default=datetime.utcnow)
