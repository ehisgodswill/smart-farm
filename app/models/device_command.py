from sqlalchemy import Column, DateTime, Enum as SQLEnum, ForeignKey, String
from datetime import datetime
from app.database import Base
from app.models.enums import ActionValueEnum

class DeviceCommand(Base):
    __tablename__ = "device_commands"

    id = Column(String, primary_key=True)
    device_id = Column(String, ForeignKey("devices.id"), nullable=False)
    action = Column(SQLEnum(ActionValueEnum), nullable=False)
    issued_by_rule = Column(String, ForeignKey("rules.id"), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
