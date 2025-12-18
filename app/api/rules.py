from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models.rule import Rule
from app.schemas.rule import RuleCreate, RuleRead
import uuid
from datetime import datetime

router = APIRouter()

# Create a rule
@router.post("/", response_model=RuleRead)
def create_rule(rule: RuleCreate):
    db = SessionLocal()
    db_rule = Rule(
        id=str(uuid.uuid4()),
        name=rule.name,
        pen_id=rule.pen_id,
        condition=rule.condition,
        action=rule.action,
        enabled=rule.enabled,
        created_at=datetime.utcnow()
    )
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    db.close()
    return db_rule

# List all rules
@router.get("/", response_model=list[RuleRead])
def list_rules():
    db = SessionLocal()
    rules = db.query(Rule).all()
    db.close()
    return rules

# Update rule
@router.put("/{rule_id}", response_model=RuleRead)
def update_rule(rule_id: str, action_value: str | None = None, enabled: bool | None = None):
    db = SessionLocal()
    rule = db.query(Rule).filter(Rule.id == rule_id).first()
    if not rule:
        db.close()
        raise HTTPException(status_code=404, detail="Rule not found")
    if action_value is not None:
        rule.action = action_value
    if enabled is not None:
        setattr(rule, "enabled", enabled)
    db.commit()
    db.refresh(rule)
    db.close()
    return rule
