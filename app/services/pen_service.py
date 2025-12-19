import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.pen import Pen
from app.schemas.pen import PenCreate, PenUpdate

def create_pen(db: Session, payload: PenCreate) -> Pen:
    pen = Pen(
        id=str(uuid.uuid4()),
        farm_id=payload.farm_id,
        name=payload.name,
        capacity=payload.capacity,
    )
    db.add(pen)
    db.commit()
    db.refresh(pen)
    return pen

def get_pen(db: Session, pen_id: str) -> Pen:
    pen = db.query(Pen).filter(Pen.id == pen_id).first()
    if not pen:
        raise HTTPException(status_code=404, detail="Pen not found")
    return pen

def get_pens(db: Session, skip: int = 0, limit: int = 100) -> list[Pen]:
    return db.query(Pen).offset(skip).limit(limit).all()

def update_pen(db: Session, pen_id: str, payload: PenUpdate) -> Pen:
    pen = get_pen(db, pen_id)
    if payload.name is not None:
        pen.name = payload.name
    if payload.capacity is not None:
        pen.capacity = payload.capacity
    db.commit()
    db.refresh(pen)
    return pen

def delete_pen(db: Session, pen_id: str) -> Pen:
    pen = get_pen(db, pen_id)
    db.delete(pen)
    db.commit()
    return pen
