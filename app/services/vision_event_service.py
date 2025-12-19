import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.vision_event import VisionEvent
from app.services.rule_engine_service import evaluate_rules_for_vision_event


def get_vision_event(db: Session, event_id: str) -> VisionEvent | None:
    return db.query(VisionEvent).filter(VisionEvent.id == event_id).first()


def get_vision_events(db: Session, skip: int = 0, limit: int = 100) -> list[VisionEvent]:
    return db.query(VisionEvent).offset(skip).limit(limit).all()


def create_vision_event(
    db: Session,
    pen_id: str,
    type: str,
    bird_id: str | None = None,
    confidence: float | None = None,
    image_url: str | None = None,
    id: str | None = None
) -> VisionEvent:
    event = VisionEvent(
        id=id or str(uuid.uuid4()),
        pen_id=pen_id,
        bird_id=bird_id,
        type=type,
        confidence=confidence,
        image_url=image_url
    )
    db.add(event)
    db.commit()
    db.refresh(event)

    # Trigger rule engine for this vision event
    evaluate_rules_for_vision_event(db, event)

    return event


def update_vision_event(
    db: Session,
    event_id: str,
    **kwargs
) -> VisionEvent | None:
    event = get_vision_event(db, event_id)
    if not event:
        return None
    for key, value in kwargs.items():
        if value is not None and hasattr(event, key):
            setattr(event, key, value)
    db.commit()
    db.refresh(event)
    return event


def delete_vision_event(db: Session, event_id: str) -> VisionEvent | None:
    event = get_vision_event(db, event_id)
    if not event:
        return None
    db.delete(event)
    db.commit()
    return event
