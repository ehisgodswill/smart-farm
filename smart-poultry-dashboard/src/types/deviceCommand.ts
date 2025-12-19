import { DeviceType, ActionValue, CommandStatus } from "./enums";

export interface DeviceCommand {
  id: string;
  device_id: string;
  device_type: DeviceType;
  action: ActionValue;
  source: string;
  rule_id?: string | null;
  status: CommandStatus;
  created_at: string;
  executed_at?: string | null;
}

export interface DeviceCommandCreate {
  device_id: string;
  action: ActionValue;
  source: "rule_engine" | "admin" | "system";
}
