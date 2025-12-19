from sqlalchemy.orm import Session
from app.models.sensor_reading import SensorReading
from app.models.rule import Rule
from app.models.enums import OperatorEnum
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

