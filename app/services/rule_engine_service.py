from sqlalchemy.orm import Session
from app.models.sensor_reading import SensorReading
from app.models.rule import Rule
from app.models.enums import ActionValueEnum, OperatorEnum
from app.models.vision_event import VisionEvent
from app.services.device_command_service import issue_device_command
from app.services.rule_action_executor import execute_device_action

OPERATORS = {
    OperatorEnum.GT: lambda a, b: a > b,
    OperatorEnum.LT: lambda a, b: a < b,
    OperatorEnum.GTE: lambda a, b: a >= b,
    OperatorEnum.LTE: lambda a, b: a <= b,
    OperatorEnum.EQ: lambda a, b: a == b,
    OperatorEnum.NEQ: lambda a, b: a != b,
}


VISION_EVENT_MAP = {
    "sick": "HEATER_ON",
    "abnormal_behavior": "ALERT",
    "aggression": "ALARM"
}

def evaluate_rules_for_sensor(db, reading):
    rules = (
        db.query(Rule)
        .filter(Rule.enabled.is_(True))
        .filter(Rule.sensor_type == reading.sensor.type)
        .filter(
            (Rule.pen_id == reading.pen_id) | (Rule.pen_id.is_(None))
        )
        .order_by(Rule.priority.desc())
        .all()
    )

    for rule in rules:
        if OPERATORS[rule.operator](reading.value, rule.threshold):
            execute_device_action(db, rule, reading)


def evaluate_rules_for_reading(db: Session, reading: SensorReading):
    """
    Evaluate all relevant rules for this sensor reading.
    Trigger device commands if rules match.
    """
    rules: list[Rule] = db.query(Rule).filter(
        Rule.sensor_type == reading.sensor.type,
        Rule.enabled == True
    ).all()

    # Include global rules (pen_id=None) and pen-specific rules
    rules = [r for r in rules if r.pen_id is None or r.pen_id == reading.pen_id]

    for rule in sorted(rules, key=lambda r: r.priority, reverse=True):
        op_func = OPERATORS.get(rule.operator)
        if op_func and op_func(reading.value, rule.threshold):
            # Trigger device action
            issue_device_command(
                db,
                device_id=f"auto-{rule.action_device}-{reading.pen_id}",
                action=rule.action_value,
                source="rule_engine",
            )

def evaluate_rules_for_vision_event(db: Session, event: VisionEvent):
    """
    Evaluate rules that respond to VisionEvents.
    Trigger device actions automatically based on the event type.
    """
    # Fetch rules that are global or pen-specific
    rules = db.query(Rule).all()  # optionally filter by pen_id if desired
    relevant_rules = [r for r in rules if r.pen_id is None or r.pen_id == event.pen_id]

    for rule in relevant_rules:
        # Map vision event type to action_value if matches
        action_value = VISION_EVENT_MAP.get(event.type)
        if action_value:
            # Trigger device command
            issue_device_command(
                db=db,
                device_id=f"auto-{rule.action_device}-{event.pen_id}",
                action=ActionValueEnum[action_value],
                source="vision_engine",
            )