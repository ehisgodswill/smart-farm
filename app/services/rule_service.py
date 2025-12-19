import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.rule import Rule


def get_rule(db: Session, rule_id: str) -> Rule | None:
    return db.query(Rule).filter(Rule.id == rule_id).first()


def get_rules(db: Session, skip: int = 0, limit: int = 100) -> list[Rule]:
    return db.query(Rule).offset(skip).limit(limit).all()


def create_rule(
    db: Session,
    sensor_type,
    operator,
    threshold,
    action_device,
    action_value,
    pen_id: str | None = None,
    priority: int = 1,
    enabled: bool = True,
    id: str | None = None
) -> Rule:
    rule = Rule(
        id=id or str(uuid.uuid4()),
        pen_id=pen_id,
        sensor_type=sensor_type,
        operator=operator,
        threshold=threshold,
        action_device=action_device,
        action_value=action_value,
        priority=priority,
        enabled=enabled
    )
    db.add(rule)
    db.commit()
    db.refresh(rule)
    return rule


def update_rule(
    db: Session,
    rule_id: str,
    **kwargs
) -> Rule | None:
    rule = get_rule(db, rule_id)
    if not rule:
        return None
    for key, value in kwargs.items():
        if value is not None and hasattr(rule, key):
            setattr(rule, key, value)
    db.commit()
    db.refresh(rule)
    return rule


def delete_rule(db: Session, rule_id: str) -> Rule | None:
    rule = get_rule(db, rule_id)
    if not rule:
        return None
    db.delete(rule)
    db.commit()
    return rule
