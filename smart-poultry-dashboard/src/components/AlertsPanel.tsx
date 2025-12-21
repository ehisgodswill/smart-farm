import { Card, Typography } from "@mui/material";
import { VisionEvent } from "../types/visionEvent";

export function AlertsPanel({ events }: { events: VisionEvent[] }) {
  return (
    <Card className="mt-6 p-4">
      <Typography variant="h6" className="font-bold mb-4 text-yellow-800">
        Alerts
      </Typography>
      <div className="flex flex-col gap-2 max-h-64 overflow-y-auto">
        {events.map((e) => (
          <div
            key={e.id}
            className="p-2 rounded bg-yellow-100 text-yellow-900 shadow-sm"
          >
            {e.type} - {new Date(e.timestamp).toLocaleTimeString()}
          </div>
        ))}
      </div>
    </Card>
  );
}
