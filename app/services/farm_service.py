import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.farm import Farm
from app.schemas.farm import FarmCreate, FarmUpdate


def create_farm(db: Session, payload: FarmCreate) -> Farm:
    farm = Farm(
        id=str(uuid.uuid4()),
        name=payload.name,
        location=payload.location,
    )
    db.add(farm)
    db.commit()
    db.refresh(farm)
    return farm


def get_farm(db: Session, farm_id: str) -> Farm | None:
    return db.query(Farm).filter(Farm.id == farm_id).first()


def get_farms(db: Session, skip: int = 0, limit: int = 100) -> list[Farm]:
    return (
        db.query(Farm)
        .order_by(Farm.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_farm(db: Session, farm_id: str, payload: FarmUpdate) -> Farm:
    farm = get_farm(db, farm_id)
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")

    if payload.name is not None:
        farm.name = payload.name
    if payload.location is not None:
        farm.location = payload.location

    db.commit()
    db.refresh(farm)
    return farm


def delete_farm(db: Session, farm_id: str) -> Farm:
    farm = get_farm(db, farm_id)
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")

    db.delete(farm)
    db.commit()
    return farm
