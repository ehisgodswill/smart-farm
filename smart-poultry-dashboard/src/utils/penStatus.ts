import { SensorReading } from "../types/sensorReading";
import { VisionEvent } from "../types/visionEvent";

export function computePenStatus(
  readings: SensorReading[],
  events: VisionEvent[]
) {
  const recentEvents = events.filter(
    (e) => Date.now() - new Date(e.timestamp).getTime() < 5 * 60_000
  );

  if (recentEvents.some((e) => e.type === "sick")) {
    return { level: "critical" as const };
  }

  const temps = readings
    .filter((r) => r.sensor_type === "temperature")
    .slice(0, 10)
    .map((r) => r.value);

  const avgTemp =
    temps.reduce((a, b) => a + b, 0) / Math.max(temps.length, 1);

  if (avgTemp > 35 || avgTemp < 18) {
    return { level: "warning" as const };
  }

  return { level: "normal" as const };
}
