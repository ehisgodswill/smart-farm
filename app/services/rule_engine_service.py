from sqlalchemy.orm import Session
from app.models.sensor_reading import SensorReading
from app.models.rule import Rule
from app.models.enums import OperatorEnum
from app.services.device_command_service import create_device_command
from app.services.rule_action_executor import execute_device_action

OPERATORS = {
    OperatorEnum.GT: lambda a, b: a > b,
    OperatorEnum.LT: lambda a, b: a < b,
    OperatorEnum.GTE: lambda a, b: a >= b,
    OperatorEnum.LTE: lambda a, b: a <= b,
    OperatorEnum.EQ: lambda a, b: a == b,
    OperatorEnum.NEQ: lambda a, b: a != b,
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
            create_device_command(
                db,
                device_id=f"auto-{rule.action_device}-{reading.pen_id}",
                device_type=rule.action_device,
                action=rule.action_value,
                source="rule_engine",
                rule_id=rule.id
            )