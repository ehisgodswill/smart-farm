from datetime import datetime, timezone
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Farm(Base):
    __tablename__ = "farms"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    location: Mapped[str] = mapped_column(
        String,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
