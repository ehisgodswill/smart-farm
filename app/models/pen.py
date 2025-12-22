from datetime import datetime, timezone
from typing import TYPE_CHECKING, List
from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.device import Device
    from app.models.farm import Farm
    from app.models.sensor import Sensor


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
    
    module_id: Mapped[str | None] = mapped_column(String, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )


    farm: Mapped["Farm"] = relationship("Farm", back_populates="pens")
    devices: Mapped[List["Device"]] = relationship("Device", back_populates="pen")
    sensors: Mapped[List["Sensor"]] = relationship("Sensor", back_populates="pen")