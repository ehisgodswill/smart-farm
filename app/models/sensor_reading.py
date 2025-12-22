from typing import TYPE_CHECKING
import uuid
from datetime import datetime, timezone
from sqlalchemy import String, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.sensor import Sensor


class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    sensor_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("sensors.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    pen_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("pens.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    value: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
        index=True
    )

    sensor: Mapped["Sensor"] = relationship(
        "Sensor",
        back_populates="readings"
    )
