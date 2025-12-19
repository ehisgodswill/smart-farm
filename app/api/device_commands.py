from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Sequence

from app.schemas.device_command import DeviceCommandCreate, DeviceCommandUpdate, DeviceCommandOut
from app.utils.db import get_db
from app.services.device_command_service import (
    create_device_command, get_device_command, get_device_commands, update_device_command, delete_device_command
)

router = APIRouter(tags=["DeviceCommands"])


@router.post("", response_model=DeviceCommandOut)
def api_create_device_command(payload: DeviceCommandCreate, db: Session = Depends(get_db)) -> DeviceCommandOut:
    return create_device_command(
        db,
        device_id=payload.device_id,
        device_type=payload.device_type,
        action=payload.action,
        source=payload.source,
        rule_id=payload.rule_id
    )


@router.get("", response_model=Sequence[DeviceCommandOut])
def api_list_device_commands(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Sequence[DeviceCommandOut]:
    return get_device_commands(db, skip=skip, limit=limit)


@router.get("/{command_id}", response_model=DeviceCommandOut)
def api_get_device_command(command_id: str, db: Session = Depends(get_db)) -> DeviceCommandOut:
    cmd = get_device_command(db, command_id)
    if not cmd:
        raise HTTPException(status_code=404, detail="Device command not found")
    return cmd


@router.put("/{command_id}", response_model=DeviceCommandOut)
def api_update_device_command(command_id: str, payload: DeviceCommandUpdate, db: Session = Depends(get_db)) -> DeviceCommandOut:
    cmd = update_device_command(db, command_id, **payload.dict(exclude_unset=True))
    if not cmd:
        raise HTTPException(status_code=404, detail="Device command not found")
    return cmd


@router.delete("/{command_id}", response_model=DeviceCommandOut)
def api_delete_device_command(command_id: str, db: Session = Depends(get_db)) -> DeviceCommandOut:
    cmd = delete_device_command(db, command_id)
    if not cmd:
        raise HTTPException(status_code=404, detail="Device command not found")
    return cmd
