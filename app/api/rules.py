from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Sequence

from app.schemas.rule import RuleCreate, RuleUpdate, RuleOut
from app.utils.db import get_db
from app.services.rule_service import (
    create_rule, get_rule, get_rules, update_rule, delete_rule
)

router = APIRouter(tags=["Rules"])


@router.post("", response_model=RuleOut)
def api_create_rule(payload: RuleCreate, db: Session = Depends(get_db)) -> RuleOut:
    return create_rule(
        db,
        pen_id=payload.pen_id,
        sensor_type=payload.sensor_type,
        operator=payload.operator,
        threshold=payload.threshold,
        action_device=payload.action_device,
        action_value=payload.action_value,
        priority=payload.priority or 1,
        enabled=payload.enabled if payload.enabled is not None else True
    )


@router.get("", response_model=Sequence[RuleOut])
def api_list_rules(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Sequence[RuleOut]:
    return get_rules(db, skip=skip, limit=limit)


@router.get("/{rule_id}", response_model=RuleOut)
def api_get_rule(rule_id: str, db: Session = Depends(get_db)) -> RuleOut:
    rule = get_rule(db, rule_id)
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    return rule


@router.put("/{rule_id}", response_model=RuleOut)
def api_update_rule(rule_id: str, payload: RuleUpdate, db: Session = Depends(get_db)) -> RuleOut:
    rule = update_rule(db, rule_id, **payload.dict(exclude_unset=True))
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    return rule


@router.delete("/{rule_id}", response_model=RuleOut)
def api_delete_rule(rule_id: str, db: Session = Depends(get_db)) -> RuleOut:
    rule = delete_rule(db, rule_id)
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    return rule
