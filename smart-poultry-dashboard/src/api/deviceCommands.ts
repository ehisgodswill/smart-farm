import { api } from "./client";
import {
  DeviceCommand,
  DeviceCommandCreate,
} from "../types/deviceCommand";

export const listDeviceCommands = (limit = 50) =>
  api<DeviceCommand[]>(`/device-commands?limit=${limit}`);

export const sendDeviceCommand = (data: DeviceCommandCreate) =>
  api<DeviceCommand>("/device-commands", {
    method: "POST",
    body: JSON.stringify(data),
  });
