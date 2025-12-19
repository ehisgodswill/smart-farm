import uuid
from datetime import datetime, timezone
from sqlalchemy import Boolean, Float, ForeignKey, Integer, String, DateTime, Enum as SQLEnum, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.enums import (
    SensorTypeEnum,
    DeviceTypeEnum,
    OperatorEnum,
    ActionValueEnum,
)


class Rule(Base):
    __tablename__ = "rules"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    pen_id: Mapped[str | None] = mapped_column(
        String,
        ForeignKey("pens.id", ondelete="CASCADE"),
        nullable=True,
        index=True  # null = global rule
    )

    sensor_type: Mapped[SensorTypeEnum] = mapped_column(
        SQLEnum(SensorTypeEnum, name="sensor_type_enum"),
        nullable=False,
        index=True
    )

    operator: Mapped[OperatorEnum] = mapped_column(
        SQLEnum(OperatorEnum, name="operator_enum"),
        nullable=False
    )

    threshold: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    action_device: Mapped[DeviceTypeEnum] = mapped_column(
        SQLEnum(DeviceTypeEnum, name="device_type_enum"),
        nullable=False
    )

    action_value: Mapped[ActionValueEnum] = mapped_column(
        SQLEnum(ActionValueEnum, name="action_value_enum"),
        nullable=False
    )

    priority: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
        index=True
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    __table_args__ = (
        Index(
            "ix_rule_lookup",
            "enabled",
            "sensor_type",
            "pen_id",
            "priority",
        ),
    )
