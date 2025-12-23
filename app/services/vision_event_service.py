import json
import uuid
from datetime import datetime, timezone
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.models.vision_event import VisionEvent
from app.schemas.vision_event import VisionEventCreate


def create_vision_event(db: Session, payload: VisionEventCreate) -> VisionEvent:
    """Create a new vision event from validated schema"""
    
    # Parse timestamp
    if payload.timestamp:
        created_at = datetime.fromisoformat(payload.timestamp)
    else:
        created_at = datetime.now(timezone.utc)
    
    # Create the event
    event = VisionEvent(
        id=str(uuid.uuid4()),
        farm_id=payload.farm_id,
        pen_id=payload.pen_id,
        event=payload.event,
        severity=payload.severity,
        confidence=payload.confidence,
        details=json.dumps(payload.details),
        created_at=created_at
    )

    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def create_vision_event_from_mqtt(db: Session, payload: dict) -> VisionEvent | None:
    """Create vision event from raw MQTT dict with validation"""
    try:
        # Validate and convert to Pydantic model
        event_data = VisionEventCreate(**payload)
        return create_vision_event(db, event_data)
    except ValidationError as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Invalid MQTT vision event data: {e}")
        logger.debug(f"Payload: {payload}")
        return None