from datetime import datetime, timezone
from sqlalchemy import String, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class VisionEvent(Base):
    __tablename__ = "vision_events"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )

    pen_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("pens.id"),
        nullable=False
    )

    bird_id: Mapped[str | None] = mapped_column(
        String,
        ForeignKey("birds.id"),
        nullable=True
    )

    type: Mapped[str] = mapped_column(
        String,
        nullable=False  # abnormal_behavior, sick, aggression
    )

    confidence: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    image_url: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
