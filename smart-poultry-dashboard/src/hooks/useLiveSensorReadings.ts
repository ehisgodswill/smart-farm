import { useEffect } from "react";
import { wsClient } from "../utils/ws";
import { SensorReading } from "../types/sensorReading";
import { queryClient } from "../utils/queryClient";

export const useLiveSensorReadings = (penId: string) => {
  useEffect(() => {
    if (!penId) return;

    wsClient.connect();

    const unsubscribe = wsClient.subscribe((event) => {
      if (event.type !== "sensor_reading") return;
      if (event.payload.pen_id !== penId) return;

      queryClient.setQueryData<SensorReading[]>(
        ["sensor-readings", penId],
        (old = []) => [event.payload, ...old].slice(0, 100)
      );
    });

    return unsubscribe;
  }, [penId]);
};
