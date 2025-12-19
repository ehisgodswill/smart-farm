from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Sequence

from app.schemas.sensor import SensorCreate, SensorUpdate, SensorOut
from app.utils.db import get_db
from app.services.sensor_service import (
    create_sensor, get_sensor, get_sensors, update_sensor, delete_sensor
)

router = APIRouter(tags=["Sensors"])


@router.post("", response_model=SensorOut)
def api_create_sensor(payload: SensorCreate, db: Session = Depends(get_db)) -> SensorOut:
    return create_sensor(
        db,
        pen_id=payload.pen_id,
        type=payload.type,
        device_id=payload.device_id
    )


@router.get("", response_model=List[SensorOut])
def api_list_sensors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Sequence[SensorOut]:
    return get_sensors(db, skip=skip, limit=limit)


@router.get("/{sensor_id}", response_model=SensorOut)
def api_get_sensor(sensor_id: str, db: Session = Depends(get_db)) -> SensorOut:
    sensor = get_sensor(db, sensor_id)
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor


@router.put("/{sensor_id}", response_model=SensorOut)
def api_update_sensor(sensor_id: str, payload: SensorUpdate, db: Session = Depends(get_db)) -> SensorOut:
    sensor = update_sensor(db, sensor_id, **payload.dict(exclude_unset=True))
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor


@router.delete("/{sensor_id}", response_model=SensorOut)
def api_delete_sensor(sensor_id: str, db: Session = Depends(get_db)) -> SensorOut:
    sensor = delete_sensor(db, sensor_id)
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor
