from datetime import datetime, timezone
from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Pen(Base):
    __tablename__ = "pens"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )

    farm_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("farms.id"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    capacity: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
