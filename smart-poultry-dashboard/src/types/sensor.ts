import { SensorType } from "./enums";

export interface Sensor {
  id: string;
  pen_id: string;
  type: SensorType;
  device_id?: string | null;
  created_at: string;
}

export interface SensorCreate {
  pen_id: string;
  type: SensorType;
  device_id?: string | null;
}
