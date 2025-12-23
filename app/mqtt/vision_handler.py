from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.services.vision_metric_service import create_vision_metric
from app.services.vision_event_service import create_vision_event
from app.services.rule_engine_service import evaluate_rules_for_vision_event


def handle_vision_message(db: Session, topic: str, payload: dict):
    msg_type = payload.get("type")

    if msg_type == "vision_metrics":
        metric = create_vision_metric(db, payload)
        evaluate_rules_for_vision_event(db, metric)

    elif msg_type == "vision_event":
        event = create_vision_event(db, payload)
        evaluate_rules_for_vision_event(db, event)

    elif msg_type == "vision_health":
        # Optional: store or just log
        print("Vision health:", payload)

    else:
        raise HTTPException(status_code=400, detail="Unknown vision message type")
