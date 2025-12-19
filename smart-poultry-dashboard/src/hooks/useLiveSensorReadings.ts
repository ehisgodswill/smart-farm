import { useEffect } from "react";
import { wsClient } from "../helper/ws";
import { SensorReading } from "../types/sensorReading";
import { queryClient } from "../helper/queryClient";

export const useLiveSensorReadings = (penId: string) => {
  useEffect(() => {
    wsClient.connect();

    const unsub = wsClient.subscribe((event) => {
      if (event.type !== "sensor_reading") return;
      if (event.payload.pen_id !== penId) return;

      queryClient.setQueryData<SensorReading[]>(
        ["sensor-readings", penId],
        (old = []) => [event.payload, ...old].slice(0, 100)
      );
    });

    return unsub;
  }, [penId]);
};
