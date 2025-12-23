from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Sequence

from app.schemas.vision_event import VisionEventCreate, VisionEventOut
from app.utils.db import get_db
from app.services.vision_event_service import create_vision_event

router = APIRouter(tags=["VisionEvents"])


@router.post("", response_model=VisionEventOut)
def api_create_vision_event(payload: VisionEventCreate, db: Session = Depends(get_db)) -> VisionEventOut:
    return create_vision_event(db, payload)

