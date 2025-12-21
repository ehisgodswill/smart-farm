from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.sensor_reading import (
    SensorReadingCreate,
    SensorReadingOut,
)
from app.utils.db import get_db
from app.services.sensor_reading_service import (
    ingest_sensor_reading,
    get_sensor_reading,
    get_sensor_readings,
)

router = APIRouter(tags=["Sensor Readings"])

@router.post("", response_model=SensorReadingOut)
def api_create_sensor_reading(
    payload: SensorReadingCreate,
    db: Session = Depends(get_db),
):
    return ingest_sensor_reading(db, payload.model_dump())

@router.get("", response_model=List[SensorReadingOut])
def api_list_sensor_readings(
    pen_id: str,
    sensor_type: str | None = None,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return get_sensor_readings(
        db,
        pen_id=pen_id,
        sensor_type=sensor_type,
        limit=limit,
    )

@router.get("/{reading_id}", response_model=SensorReadingOut)
def api_get_sensor_reading(
    reading_id: str,
    db: Session = Depends(get_db),
):
    reading = get_sensor_reading(db, reading_id)
    if not reading:
        raise HTTPException(status_code=404, detail="Sensor reading not found")
    return reading
