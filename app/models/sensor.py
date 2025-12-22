from typing import List
import uuid
from datetime import datetime, timezone
from sqlalchemy import String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import SensorTypeEnum
from app.models.pen import Pen
from app.models.sensor_reading import SensorReading


class Sensor(Base):
    __tablename__ = "sensors"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    pen_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("pens.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    type: Mapped[SensorTypeEnum] = mapped_column(
        SQLEnum(SensorTypeEnum, name="sensor_type_enum"),
        nullable=False
    )

    device_id: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    pen: Mapped[Pen] = relationship("Pen", back_populates="sensors")

    readings: Mapped[List[SensorReading]] = relationship(
        "SensorReading",
        back_populates="sensor",
        cascade="all, delete-orphan"
    )
