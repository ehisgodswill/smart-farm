from typing import TYPE_CHECKING
import uuid
from datetime import datetime, timezone

from sqlalchemy import ForeignKey, String, DateTime, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import ActionValueEnum

if TYPE_CHECKING:
    from app.models.device import Device


class DeviceCommand(Base):
    __tablename__ = "device_commands"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    device_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("devices.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    pen_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("pens.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    action: Mapped[ActionValueEnum] = mapped_column(
        SQLEnum(ActionValueEnum, name="action_value_enum"),
        nullable=False
    )

    source: Mapped[str] = mapped_column(
        String,
        nullable=False  # rule | admin | system |manual | safety | ai
    )

    issued_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )


    device: Mapped["Device"] = relationship("Device", back_populates="commands")

