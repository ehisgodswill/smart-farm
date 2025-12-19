import { VisionEvent } from "./visionEvent";
import { SensorReading } from "./sensorReading";
import { DeviceCommand } from "./deviceCommand";

export type WSEvent =
  | VisionEventMessage
  | SensorReadingMessage
  | DeviceCommandMessage;

export interface VisionEventMessage {
  type: "vision_event";
  payload: VisionEvent;
}

export interface SensorReadingMessage {
  type: "sensor_reading";
  payload: SensorReading;
}

export interface DeviceCommandMessage {
  type: "device_command";
  payload: DeviceCommand;
}
