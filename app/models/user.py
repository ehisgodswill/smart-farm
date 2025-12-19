from sqlalchemy import Column, DateTime, Enum as SQLEnum, String
from datetime import datetime
from app.database import Base
from app.models.enums import UserRoleEnum

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(SQLEnum(UserRoleEnum), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
