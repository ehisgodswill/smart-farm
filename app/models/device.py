from sqlalchemy import Column, DateTime, Enum as SQLEnum, ForeignKey, String
from app.database import Base
from app.models.enums import DeviceTypeEnum, ActionValueEnum

class Device(Base):
    __tablename__ = "devices"

    id = Column(String, primary_key=True)
    pen_id = Column(String, ForeignKey("pens.id"), nullable=False)
    type = Column(SQLEnum(DeviceTypeEnum), nullable=False)
    state = Column(SQLEnum(ActionValueEnum), default=ActionValueEnum.OFF)
    last_command_at = Column(DateTime)
