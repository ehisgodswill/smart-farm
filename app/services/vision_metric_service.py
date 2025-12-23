from datetime import datetime
from sqlalchemy.orm import Session

from app.models.vision_metric import VisionMetric


def create_vision_metric(db: Session, payload: dict) -> VisionMetric:
    metric = VisionMetric(
        farm_id=payload["farm_id"],
        pen_id=payload["pen_id"],
        bird_count=payload["bird_count"],
        activity_level=payload["activity_level"],
        distribution_score=payload["distribution_score"],
        heat_stress_index=payload["heat_stress_index"],
        cold_stress_index=payload["cold_stress_index"],
        created_at=datetime.fromisoformat(payload["timestamp"].replace("Z", "+00:00"))
    )

    db.add(metric)
    db.commit()
    db.refresh(metric)
    return metric
