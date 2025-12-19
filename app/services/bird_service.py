from sqlalchemy.orm import Session
from app.models.bird import Bird
from datetime import date
import uuid

def get_bird(db: Session, bird_id: str) -> Bird | None:
    return db.query(Bird).filter(Bird.id == bird_id).first()

def list_birds(db: Session, skip: int = 0, limit: int = 100) -> list[Bird]:
    return db.query(Bird).offset(skip).limit(limit).all()

def create_bird(
    db: Session,
    pen_id: str,
    tag_id: str | None = None,
    hatch_date: date | None = None,
    age_days: int | None = None,
    health_score: float | None = None,
    status: str = "healthy",
    id: str | None = None
) -> Bird:
    bird = Bird(
        id=id or str(uuid.uuid4()),
        pen_id=pen_id,
        tag_id=tag_id,
        hatch_date=hatch_date,
        age_days=age_days,
        health_score=health_score,
        status=status
    )
    db.add(bird)
    db.commit()
    db.refresh(bird)
    return bird

def update_bird(
    db: Session,
    bird_id: str,
    **kwargs
) -> Bird | None:
    bird = get_bird(db, bird_id)
    if not bird:
        return None
    for key, value in kwargs.items():
        if hasattr(bird, key):
            setattr(bird, key, value)
    db.commit()
    db.refresh(bird)
    return bird

def delete_bird(db: Session, bird_id: str) -> Bird | None:
    bird = get_bird(db, bird_id)
    if not bird:
        return None
    db.delete(bird)
    db.commit()
    return bird
