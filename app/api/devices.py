from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.device import DeviceCreate, DeviceUpdate, DeviceOut
from app.utils.db import get_db
from app.services.device_service import (
    create_device, get_device, get_devices, update_device, delete_device
)

router = APIRouter(tags=["Devices"])


@router.post("", response_model=DeviceOut)
def api_create_device(payload: DeviceCreate, db: Session = Depends(get_db)) -> DeviceOut:
    return create_device(
        db,
        pen_id=payload.pen_id,
        type=payload.type,
        state=payload.state,
        last_command_at=payload.last_command_at
    )


from typing import Sequence

@router.get("", response_model=List[DeviceOut])
def api_list_devices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Sequence[DeviceOut]:
    return get_devices(db, skip=skip, limit=limit)


@router.get("/{device_id}", response_model=DeviceOut)
def api_get_device(device_id: str, db: Session = Depends(get_db)) -> DeviceOut:
    device = get_device(db, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device


@router.put("/{device_id}", response_model=DeviceOut)
def api_update_device(device_id: str, payload: DeviceUpdate, db: Session = Depends(get_db)) -> DeviceOut:
    device = update_device(db, device_id, **payload.dict(exclude_unset=True))
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device


@router.delete("/{device_id}", response_model=DeviceOut)
def api_delete_device(device_id: str, db: Session = Depends(get_db)) -> DeviceOut:
    device = delete_device(db, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device
