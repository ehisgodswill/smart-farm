from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Sequence

from app.schemas.bird import BirdCreate, BirdUpdate, BirdOut
from app.utils.db import get_db
from app.services.bird_service import create_bird, get_bird, update_bird, list_birds, delete_bird

router = APIRouter(tags=["Birds"])


@router.post("", response_model=BirdOut)
def api_create_bird(payload: BirdCreate, db: Session = Depends(get_db)) -> BirdOut:
    return create_bird(
        db,
        pen_id=payload.pen_id,
        tag_id=payload.tag_id,
        hatch_date=payload.hatch_date,
        age_days=payload.age_days,
        health_score=payload.health_score,
        status=payload.status
    )


@router.get("", response_model=List[BirdOut])
def api_list_birds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) ->Sequence[BirdOut]:
    return list_birds(db, skip=skip, limit=limit)


@router.get("/{bird_id}", response_model=BirdOut)
def api_get_bird(bird_id: str, db: Session = Depends(get_db)) -> BirdOut:
    bird = get_bird(db, bird_id)
    if not bird:
        raise HTTPException(status_code=404, detail="Bird not found")
    return bird


@router.put("/{bird_id}", response_model=BirdOut)
def api_update_bird(bird_id: str, payload: BirdUpdate, db: Session = Depends(get_db)) -> BirdOut:
    bird = update_bird(db, bird_id, **payload.dict(exclude_unset=True))
    if not bird:
        raise HTTPException(status_code=404, detail="Bird not found")
    return bird


@router.delete("/{bird_id}", response_model=BirdOut)
def api_delete_bird(bird_id: str, db: Session = Depends(get_db)) -> BirdOut:
    bird = delete_bird(db, bird_id)
    if not bird:
        raise HTTPException(status_code=404, detail="Bird not found")
    return bird
