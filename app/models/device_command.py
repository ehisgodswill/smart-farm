import uuid
from datetime import datetime, timezone

from sqlalchemy import ForeignKey, String, DateTime, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.enums import DeviceTypeEnum, ActionValueEnum, CommandStatusEnum


class DeviceCommand(Base):
    __tablename__ = "device_commands"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    device_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
        index=True
    )

    device_type: Mapped[DeviceTypeEnum] = mapped_column(
        SQLEnum(DeviceTypeEnum, name="device_type_enum"),
        nullable=False
    )

    action: Mapped[ActionValueEnum] = mapped_column(
        SQLEnum(ActionValueEnum, name="action_value_enum"),
        nullable=False
    )

    source: Mapped[str] = mapped_column(
        String,
        nullable=False  # rule_engine | admin | system
    )

    rule_id: Mapped[str | None] = mapped_column(
        String,
        ForeignKey("rules.id"),
        nullable=True
    )

    status: Mapped[CommandStatusEnum] = mapped_column(
        SQLEnum(CommandStatusEnum, name="command_status_enum"),
        default=CommandStatusEnum.pending,
        index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    executed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
