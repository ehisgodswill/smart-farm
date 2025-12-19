from datetime import date, datetime, timezone

from sqlalchemy import Date, Float, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Bird(Base):
    __tablename__ = "birds"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    pen_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("pens.id"),
        nullable=False,
    )

    tag_id: Mapped[str | None] = mapped_column(
        String,
        unique=True,
        nullable=True,
    )

    hatch_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    age_days: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    health_score: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String,
        default="healthy",
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
