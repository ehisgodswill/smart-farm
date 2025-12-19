import {
  SensorType,
  DeviceType,
  Operator,
  ActionValue,
} from "./enums";

export interface Rule {
  id: string;
  pen_id?: string | null;
  sensor_type: SensorType;
  operator: Operator;
  threshold: number;
  action_device: DeviceType;
  action_value: ActionValue;
  priority: number;
  enabled: boolean;
  created_at: string;
}

export interface RuleCreate {
  pen_id?: string | null;
  sensor_type: SensorType;
  operator: Operator;
  threshold: number;
  action_device: DeviceType;
  action_value: ActionValue;
  priority?: number;
}

export interface RuleUpdate {
  threshold?: number;
  priority?: number;
  enabled?: boolean;
}
