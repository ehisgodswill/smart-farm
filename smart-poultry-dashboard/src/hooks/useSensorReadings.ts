import { useQuery } from "@tanstack/react-query";
import { api } from "../utils/api";
import { SensorReading } from "../types/sensorReading";

export const useSensorReadings = (penId: string) => {
  return useQuery<SensorReading[]>({
    queryKey: ["sensor-readings", penId],
    queryFn: () =>
      api<SensorReading[]>(
        `/sensor-readings?pen_id=${penId}&limit=100`
      ),
    refetchInterval: 30_000,
    enabled: !!penId,
  });
}
