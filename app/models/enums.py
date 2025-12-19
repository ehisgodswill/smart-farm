from enum import Enum

# Sensors
class SensorTypeEnum(str, Enum):
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    WATER = "water"
    FEED = "feed"

# Devices
class DeviceTypeEnum(str, Enum):
    FAN = "fan"
    HEATER = "heater"
    FEEDER = "feeder"
    LIGHT = "light"

# Rule operators
class OperatorEnum(str, Enum):
    GREATER = ">"
    LESS = "<"
    GREATER_EQUAL = ">="
    LESS_EQUAL = "<="
    EQUAL = "=="

# User roles
class UserRoleEnum(str, Enum):
    ADMIN = "admin"
    OPERATOR = "operator"

# Device action states
class ActionValueEnum(str, Enum):
    ON = "ON"
    OFF = "OFF"
