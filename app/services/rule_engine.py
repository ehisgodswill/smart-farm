from app.database import SessionLocal
from app.models.rule import Rule
from app.mqtt.client import send_device_command

OPERATOR_MAP = {
    ">": lambda x, y: x > y,
    "<": lambda x, y: x < y,
    ">=": lambda x, y: x >= y,
    "<=": lambda x, y: x <= y,
    "==": lambda x, y: x == y
}

def evaluate_rules(pen_id, sensor_type, value):
    db = SessionLocal()
    rules = db.query(Rule).filter(
        Rule.enabled == True,
        Rule.sensor_type == sensor_type,
    ).all()
    
    for rule in rules:
        if rule.pen_id is not None and rule.pen_id != pen_id:
            continue
        
        if OPERATOR_MAP[getattr(rule, "operator")](value, rule.threshold):
            send_device_command(
                device_id=f"esp32-sim-01",  # map pen_id → device_id
                pen_id=pen_id,
                device=rule.action_device,
                action=rule.action_value
            )
            print(f"Rule triggered: {rule.id} | {sensor_type}={value}")
    
    db.close()
