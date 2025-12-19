interface Alert {
  id: string;
  type: string; // sick, sensor_high, device_failed
  message: string;
  pen_id: string;
  timestamp: string;
}

interface AlertsPanelProps {
  alerts: Alert[];
}

export function AlertsPanel({ alerts }: AlertsPanelProps) {
  return (
    <div className="bg-gray-900 text-white p-4 rounded shadow-md">
      <h3 className="text-lg font-bold mb-2">Alerts</h3>
      {alerts.length === 0 ? (
        <p className="text-gray-400">No alerts</p>
      ) : (
        <ul className="space-y-2 max-h-64 overflow-y-auto">
          {alerts.map((alert) => (
            <li key={alert.id} className="flex justify-between items-center border-b border-gray-700 pb-1">
              <span className="text-sm">{alert.message}</span>
              <span className="text-xs text-gray-400">{new Date(alert.timestamp).toLocaleTimeString()}</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
