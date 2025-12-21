from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Sequence

from app.utils.db import get_db
from app.schemas.farm import FarmCreate, FarmUpdate, FarmOut
from app.services.farm_service import (
    create_farm,
    get_farm,
    get_farms,
    update_farm,
    delete_farm,
)

router = APIRouter(tags=["Farms"])


@router.post("", response_model=FarmOut)
def api_create_farm(
    payload: FarmCreate,
    db: Session = Depends(get_db),
) -> FarmOut:
    return create_farm(db, payload)


@router.get("", response_model=List[FarmOut])
def api_list_farms(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> Sequence[FarmOut]:
    return get_farms(db, skip, limit)


@router.get("/{farm_id}", response_model=FarmOut)
def api_get_farm(
    farm_id: str,
    db: Session = Depends(get_db),
) -> FarmOut:
    farm = get_farm(db, farm_id)
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    return farm


@router.put("/{farm_id}", response_model=FarmOut)
def api_update_farm(
    farm_id: str,
    payload: FarmUpdate,
    db: Session = Depends(get_db),
) -> FarmOut:
    return update_farm(db, farm_id, payload)


@router.delete("/{farm_id}", response_model=FarmOut)
def api_delete_farm(
    farm_id: str,
    db: Session = Depends(get_db),
) -> FarmOut:
    return delete_farm(db, farm_id)
