import { api } from "../utils/api";
import { Device, DeviceCreate } from "../types/device";

export const listDevices = (penId: string) =>
  api<Device[]>(`/devices/pen/${penId}`);

export const createDevice = (payload: DeviceCreate) =>
  api<Device>("/devices", {
    method: "POST",
    body: JSON.stringify(payload),
  });

export const updateDevice = (id: string, payload: Partial<Device>) =>
  api<Device>(`/devices/${id}`, {
    method: "PUT",
    body: JSON.stringify(payload),
  });

export const deleteDevice = (id: string) =>
  api<Device>(`/devices/${id}`, { method: "DELETE" });
