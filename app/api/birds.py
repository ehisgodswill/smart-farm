from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.bird import BirdCreate, BirdUpdate, BirdOut
from app.utils.db import get_db
from app.services.bird_service import create_bird, get_bird, update_bird, get_birds, delete_bird

router = APIRouter(tags=["Birds"])

@router.post("", response_model=BirdOut)
def api_create_bird(payload: BirdCreate, db: Session = Depends(get_db)):
    return create_bird(db, payload)

@router.get("", response_model=list[BirdOut])
def api_list_birds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_birds(db, skip, limit)

@router.get("/{bird_id}", response_model=BirdOut)
def api_get_bird(bird_id: int, db: Session = Depends(get_db)):
    return get_bird(db, bird_id)

@router.put("/{bird_id}", response_model=BirdOut)
def api_update_bird(bird_id: int, payload: BirdUpdate, db: Session = Depends(get_db)):
    return update_bird(db, bird_id, payload)

@router.delete("/{bird_id}", response_model=BirdOut)
def api_delete_bird(bird_id: int, db: Session = Depends(get_db)):
    return delete_bird(db, bird_id)
