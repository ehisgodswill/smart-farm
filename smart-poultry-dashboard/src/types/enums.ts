export enum SensorType {
  TEMPERATURE = "temperature",
  HUMIDITY = "humidity",
  AMMONIA = "ammonia",
  LIGHT = "light",
  MOTION = "motion",
}

export enum DeviceType {
  FEEDER = "feeder",
  FAN = "fan",
  LIGHT = "light",
  HEATER = "heater",
}

export enum ActionValue {
  ON = "on",
  OFF = "off",
}

export enum Operator {
  GT = ">",
  GTE = ">=",
  LT = "<",
  LTE = "<=",
  EQ = "==",
}

export enum CommandStatus {
  PENDING = "pending",
  EXECUTED = "executed",
  FAILED = "failed",
}

export enum UserRole {
  ADMIN = "admin",
  MANAGER = "manager",
  WORKER = "worker",
}
