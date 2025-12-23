from sqlalchemy.orm import Session
from typing import Any
import logging

from app.services.vision_metric_service import create_vision_metric
from app.services.vision_event_service import create_vision_event, create_vision_event_from_mqtt
from app.services.rule_engine_service import evaluate_rules_for_vision_event

logger = logging.getLogger(__name__)


def handle_vision_message(db: Session, topic: str, payload: dict[str, Any]) -> None:
    """
    Handle incoming vision messages from MQTT
    
    Args:
        db: Database session
        topic: MQTT topic the message was received on
        payload: Decoded message payload
    """
    msg_type = payload.get("type")

    try:
        if msg_type == "vision_metrics":
            logger.info(f"Processing vision metrics from {topic}")
            metric = create_vision_metric(db, payload)
            evaluate_rules_for_vision_event(db, metric)
            logger.info(f"Vision metric created: {metric.id}")

        elif msg_type == "vision_event":
            logger.info(f"Processing vision event from {topic}")
            event = create_vision_event_from_mqtt(db, payload)
            evaluate_rules_for_vision_event(db, event)
            logger.info(f"Vision event created: {event}")

        elif msg_type == "vision_health":
            # Store health status or just log
            logger.info(f"Vision health check: {payload}")
            # Optional: Store in a health_status table
            # create_health_check(db, payload)

        else:
            logger.warning(f"Unknown vision message type: {msg_type}")
            # Don't raise HTTPException in MQTT handler - just log and continue
            
    except KeyError as e:
        logger.error(f"Missing required field in vision message: {e}")
        logger.debug(f"Payload: {payload}")
    except Exception as e:
        logger.error(f"Error processing vision message: {e}", exc_info=True)
        # Don't raise - MQTT handler should be resilient
        # Optionally: Store failed messages for retry