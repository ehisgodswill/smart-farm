from datetime import datetime
from sqlalchemy.orm import Session
import json

from app.models.vision_event import VisionEvent


def create_vision_event(db: Session, payload: dict) -> VisionEvent:
    event = VisionEvent(
        farm_id=payload["farm_id"],
        pen_id=payload["pen_id"],
        event=payload["event"],
        severity=payload["severity"],
        confidence=payload["confidence"],
        details=json.dumps(payload.get("details", {})),
        created_at=datetime.fromisoformat(payload["timestamp"].replace("Z", "+00:00"))
    )

    db.add(event)
    db.commit()
    db.refresh(event)
    return event
