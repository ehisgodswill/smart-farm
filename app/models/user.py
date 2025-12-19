from datetime import datetime, timezone
from sqlalchemy import String, DateTime, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.enums import UserRoleEnum


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )

    username: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    role: Mapped[UserRoleEnum] = mapped_column(
        SQLEnum(UserRoleEnum, name="user_role_enum"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
