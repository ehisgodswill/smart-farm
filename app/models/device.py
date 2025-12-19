from datetime import datetime, timezone
from sqlalchemy import ForeignKey, String, DateTime, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.enums import DeviceTypeEnum, ActionValueEnum


class Device(Base):
    __tablename__ = "devices"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )

    pen_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("pens.id"),
        nullable=False
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
