import { api } from "../utils/api";
import {
  SensorReading,
  SensorReadingIngest,
} from "../types/sensorReading";

export const ingestSensorReading = (data: SensorReadingIngest) =>
  api<SensorReading>("/sensor-readings", {
    method: "POST",
    body: JSON.stringify(data),
  });

export const listSensorReadings = (penId: string, limit = 50) =>
  api<SensorReading[]>(
    `/sensor-readings?pen_id=${penId}&limit=${limit}`
  );
