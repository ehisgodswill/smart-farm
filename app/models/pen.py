from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from app.database import Base
from datetime import datetime


class Pen(Base):
    __tablename__ = "pens"

    id = Column(String, primary_key=True)
    farm_id = Column(String, ForeignKey("farms.id"))
    name = Column(String)
    capacity = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
