from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Sequence

from app.schemas.device import DeviceCreate, DeviceOut
from app.utils.db import get_db
from app.services.device_service import (
    create_device,
    get_devices_by_pen,
    get_device,
    delete_device
)

router = APIRouter(tags=["Devices"])

@router.post("/pens/{pen_id}", response_model=DeviceOut)
def api_create_device(
    pen_id: str,
    payload: DeviceCreate,
    db: Session = Depends(get_db)
) -> DeviceOut:
    return create_device(
        db,
        pen_id=pen_id,
        type=payload.type
    )

@router.get("/pens/{pen_id}", response_model=List[DeviceOut])
def api_list_devices_by_pen(
    pen_id: str,
    db: Session = Depends(get_db)
) -> Sequence[DeviceOut]:
    return get_devices_by_pen(db, pen_id)

@router.get("/{device_id}", response_model=DeviceOut)
def api_get_device(
    device_id: str,
    db: Session = Depends(get_db)
) -> DeviceOut:
    device = get_device(db, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@router.delete("/{device_id}", response_model=DeviceOut)
def api_delete_device(
    device_id: str,
    db: Session = Depends(get_db)
) -> DeviceOut:
    device = delete_device(db, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device
