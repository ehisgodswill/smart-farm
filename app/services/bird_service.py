from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.bird import Bird
from app.schemas.bird import BirdCreate, BirdUpdate
from fastapi import HTTPException

# -----------------------------
# Create
# -----------------------------
def create_bird(db: Session, bird_data: BirdCreate) -> Bird:
    bird = Bird(**bird_data.model_dump())
    db.add(bird)
    try:
        db.commit()
        db.refresh(bird)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Bird tag_id must be unique")
    return bird

# -----------------------------
# Read / List
# -----------------------------
def get_birds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Bird).offset(skip).limit(limit).all()

def get_bird(db: Session, bird_id: int):
    bird = db.query(Bird).filter(Bird.id == bird_id).first()
    if not bird:
        raise HTTPException(status_code=404, detail="Bird not found")
    return bird

# -----------------------------
# Update
# -----------------------------
def update_bird(db: Session, bird_id: int, bird_data: BirdUpdate):
    bird = get_bird(db, bird_id)
    for key, value in bird_data.model_dump(exclude_unset=True).items():
        setattr(bird, key, value)
    db.commit()
    db.refresh(bird)
    return bird

# -----------------------------
# Delete / Soft Delete
# -----------------------------
def delete_bird(db: Session, bird_id: int):
    bird = get_bird(db, bird_id)
    bird.is_active = False  # soft delete
    db.commit()
    db.refresh(bird)
    return bird
