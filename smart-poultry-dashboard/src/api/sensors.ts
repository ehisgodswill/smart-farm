import { api } from "./client";
import { Sensor, SensorCreate } from "../types/sensor";

export const listSensors = (penId?: string) =>
  api<Sensor[]>(penId ? `/sensors?pen_id=${penId}` : "/sensors");

export const createSensor = (data: SensorCreate) =>
  api<Sensor>("/sensors", {
    method: "POST",
    body: JSON.stringify(data),
  });

export const deleteSensor = (id: string) =>
  api<Sensor>(`/sensors/${id}`, { method: "DELETE" });
