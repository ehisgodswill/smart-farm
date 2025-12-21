import { api } from "../utils/api";
import { Device, DeviceCreate } from "../types/device";

export const listDevices = (penId?: string) =>
  api<Device[]>(penId ? `/devices?pen_id=${penId}` : "/devices");

export const createDevice = (data: DeviceCreate) =>
  api<Device>("/devices", {
    method: "POST",
    body: JSON.stringify(data),
  });

export const deleteDevice = (id: string) =>
  api<Device>(`/devices/${id}`, { method: "DELETE" });
