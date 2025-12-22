from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlalchemy import ForeignKey, String, DateTime, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import DeviceTypeEnum, ActionValueEnum

if TYPE_CHECKING:
    from app.models.device_command import DeviceCommand
    from app.models.pen import Pen


class Device(Base):
    __tablename__ = "devices"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )

    pen_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("pens.id", ondelete="CASCADE"),
        nullable=False,
    )

    type: Mapped[DeviceTypeEnum] = mapped_column(
        SQLEnum(DeviceTypeEnum, name="device_type_enum"),
        nullable=False
    )

    state: Mapped[ActionValueEnum] = mapped_column(
        SQLEnum(ActionValueEnum, name="action_value_enum"),
        default=ActionValueEnum.OFF,
        nullable=False
    )

    last_command_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    pen: Mapped["Pen"] = relationship("Pen", back_populates="devices")

    commands: Mapped[List["DeviceCommand"]] = relationship("DeviceCommand", back_populates="device")