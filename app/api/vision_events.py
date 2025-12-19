from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Sequence

from app.schemas.vision_event import VisionEventCreate, VisionEventUpdate, VisionEventOut
from app.utils.db import get_db
from app.services.vision_event_service import (
    create_vision_event, get_vision_event, get_vision_events, update_vision_event, delete_vision_event
)

router = APIRouter(tags=["VisionEvents"])


@router.post("", response_model=VisionEventOut)
def api_create_vision_event(payload: VisionEventCreate, db: Session = Depends(get_db)) -> VisionEventOut:
    return create_vision_event(
        db,
        pen_id=payload.pen_id,
        bird_id=payload.bird_id,
        type=payload.type,
        confidence=payload.confidence,
        image_url=payload.image_url
    )


@router.get("", response_model=Sequence[VisionEventOut])
def api_list_vision_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Sequence[VisionEventOut]:
    return get_vision_events(db, skip=skip, limit=limit)


@router.get("/{event_id}", response_model=VisionEventOut)
def api_get_vision_event(event_id: str, db: Session = Depends(get_db)) -> VisionEventOut:
    event = get_vision_event(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Vision event not found")
    return event


@router.put("/{event_id}", response_model=VisionEventOut)
def api_update_vision_event(event_id: str, payload: VisionEventUpdate, db: Session = Depends(get_db)) -> VisionEventOut:
    event = update_vision_event(db, event_id, **payload.dict(exclude_unset=True))
    if not event:
        raise HTTPException(status_code=404, detail="Vision event not found")
    return event


@router.delete("/{event_id}", response_model=VisionEventOut)
def api_delete_vision_event(event_id: str, db: Session = Depends(get_db)) -> VisionEventOut:
    event = delete_vision_event(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Vision event not found")
    return event
