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

export default function Dashboard() {
  const { penId } = useParams<{ penId: string }>();

  const { data: readings = [] } = useSensorReadings(penId!);
  const { data: events = [] } = useVisionEvents(penId!);
  const { data: commands = [] } = useDeviceCommands(penId!);

  useLiveSensorReadings(penId!);
  useLiveVisionEvents();
  useLiveDeviceCommands();

  const status = computePenStatus( readings, events);

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-green-800">Pen {penId}</h2>
      <div className="flex gap-4 items-center mb-4">
        <span className={`px-3 py-1 rounded-full font-bold ${status.level === "normal" ? "bg-green-400 text-white" :
            status.level === "warning" ? "bg-yellow-400 text-white" :
              "bg-red-500 text-white"
          }`}>
          Status: {status.level.toUpperCase()}
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
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
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-4">
        <AlertsPanel events={events} />
        <DeviceActionsLog commands={commands} />
      </div>
    </div>
  );
}
