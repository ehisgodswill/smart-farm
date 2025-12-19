from sqlalchemy import Column, DateTime, String
from app.database import Base
from datetime import datetime

class Farm(Base):
    __tablename__ = "farms"

    id = Column(String, primary_key=True)
    name = Column(String)
    location = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
