import { SensorType } from "./enums";

export interface SensorReading {
  id: string;
  sensor_id: string;
  sensor_type: SensorType;
  pen_id: string;
  value: number;
  timestamp: string;
}

export interface SensorReadingIngest {
  sensor_id: string;
  pen_id: string;
  value: number;
  timestamp?: string;
}
