from datetime import datetime, timezone
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class VisionMetric(Base):
    __tablename__ = "vision_metrics"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    farm_id: Mapped[str] = mapped_column(String, nullable=False)
    pen_id: Mapped[str] = mapped_column(String, nullable=False)

    bird_count: Mapped[int] = mapped_column(Integer, nullable=False)
    activity_level: Mapped[float] = mapped_column(Float, nullable=False)
    distribution_score: Mapped[float] = mapped_column(Float, nullable=False)

    heat_stress_index: Mapped[float] = mapped_column(Float, nullable=True)
    cold_stress_index: Mapped[float] = mapped_column(Float, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
