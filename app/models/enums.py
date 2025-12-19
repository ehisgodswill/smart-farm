from enum import Enum

class SensorTypeEnum(str, Enum):
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    LIGHT = "light"
    WATER = "water"
    FEED = "feed"

class DeviceTypeEnum(str, Enum):
    FAN = "fan"
    FEEDER = "feeder"
    LIGHT = "light"
    ALARM = "alarm"

class OperatorEnum(str, Enum):
    GT = ">"
    LT = "<"
    GTE = ">="
    LTE = "<="
    EQ = "=="
    NEQ = "!="

class UserRoleEnum(str, Enum):
    ADMIN = "admin"
    OPERATOR = "operator"

class ActionValueEnum(str, Enum):
    ON = "ON"
    OFF = "OFF"

class CommandStatusEnum(str, Enum):
    pending = "pending"
    sent = "sent"
    failed = "failed"
    acknowledged = "acknowledged"