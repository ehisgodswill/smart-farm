import { DeviceType, ActionValue } from "./enums";

export interface Device {
  id: string;
  pen_id: string;
  type: DeviceType;
  state: ActionValue;
  last_command_at?: string | null;
}

export interface DeviceCreate {
  pen_id: string;
  type: DeviceType;
}
