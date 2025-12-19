from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.pen import PenCreate, PenUpdate, PenOut
from app.services.pen_service import create_pen, get_pen, get_pens, update_pen, delete_pen
from app.utils.db import get_db

router = APIRouter(tags=["Pens"], prefix="/api/pens")

@router.post("", response_model=PenOut)
def api_create_pen(payload: PenCreate, db: Session = Depends(get_db)):
    return create_pen(db, payload)

@router.get("", response_model=list[PenOut])
def api_list_pens(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_pens(db, skip, limit)

@router.get("/{pen_id}", response_model=PenOut)
def api_get_pen(pen_id: str, db: Session = Depends(get_db)):
    return get_pen(db, pen_id)

@router.put("/{pen_id}", response_model=PenOut)
def api_update_pen(pen_id: str, payload: PenUpdate, db: Session = Depends(get_db)):
    return update_pen(db, pen_id, payload)

@router.delete("/{pen_id}", response_model=PenOut)
def api_delete_pen(pen_id: str, db: Session = Depends(get_db)):
    return delete_pen(db, pen_id)
