import { useParams } from "react-router-dom";
import { useSensorReadings } from "../hooks/useSensorReadings";
import { useVisionEvents } from "../hooks/useVisionEvents";
import { useDeviceCommands } from "../hooks/useDeviceCommands";
import { useLiveSensorReadings } from "../hooks/useLiveSensorReadings";
import { useLiveVisionEvents } from "../hooks/useLiveVisionEvents";
import { useLiveDeviceCommands } from "../hooks/useLiveDeviceCommands";

import { LiveSensorChart } from "../components/LiveSensorCharts";
import { AlertsPanel } from "../components/AlertsPanel";
import { DeviceActionsLog } from "../components/DeviceActionsLog";
import { computePenStatus } from "../utils/penStatus";

export function PenDashboard() {
  const { penId } = useParams<{ penId: string }>();

  const { data: readings = [] } = useSensorReadings(penId!);
  const { data: events = [] } = useVisionEvents(penId!);
  const { data: commands = [] } = useDeviceCommands(penId!);

  useLiveSensorReadings(penId!);
  useLiveVisionEvents();
  useLiveDeviceCommands();

  const status = computePenStatus(readings, events);

  return (
    <div>
      <h2>Pen {penId}</h2>

      <div>Status: {status.level.toUpperCase()}</div>

      <LiveSensorChart
        readings={readings.filter((r) => r.sensor_type === "temperature")}
        label="Temperature"
        unit="°C"
      />

      <LiveSensorChart
        readings={readings.filter((r) => r.sensor_type === "humidity")}
        label="Humidity"
        unit="%"
      />

      <AlertsPanel events={events} />
      <DeviceActionsLog commands={commands} />
    </div>
  );
}
