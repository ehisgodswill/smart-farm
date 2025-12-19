from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models.rule import Rule
from app.schemas.rule import RuleCreate, RuleRead

router = APIRouter()

# Create rule
@router.post("", response_model=RuleRead)
def create_rule(rule: RuleCreate):
    db = SessionLocal()

    db_rule = Rule(
        name=rule.name,
        pen_id=rule.pen_id,
        condition=rule.condition,
        action=rule.action,
        enabled=rule.enabled,
        priority=rule.priority
    )

    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    db.close()
    return db_rule


# List rules
@router.get("", response_model=list[RuleRead])
def list_rules():
    db = SessionLocal()
    rules = db.query(Rule).order_by(Rule.priority.desc()).all()
    db.close()
    return rules


# Update rule
@router.put("/{rule_id}", response_model=RuleRead)
def update_rule(
    rule_id: str,
    name: str | None = None,
    action: str | None = None,
    enabled: bool | None = None,
    priority: float | None = None
):
    db = SessionLocal()
    rule = db.query(Rule).filter(Rule.id == rule_id).first()

    if not rule:
        db.close()
        raise HTTPException(status_code=404, detail="Rule not found")

    if name is not None:
        setattr(rule, "name", name)
    if action is not None:
        setattr(rule, "action", action)
    if enabled is not None:
        setattr(rule, "enabled", enabled)
    if priority is not None:
        setattr(rule, "priority", priority)

    db.commit()
    db.refresh(rule)
    db.close()
    return rule
