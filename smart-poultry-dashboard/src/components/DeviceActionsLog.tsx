import { Card, Typography } from "@mui/material";
import { DeviceCommand } from "../types/deviceCommand";

export function DeviceActionsLog({ commands }: { commands: DeviceCommand[] }) {
  return (
    <Card className="mt-6 p-4">
      <Typography variant="h6" className="font-bold mb-4 text-green-800">
        Device Actions
      </Typography>
      <div className="flex flex-col gap-2 max-h-64 overflow-y-auto">
        {commands.map((c) => (
          <div
            key={c.id}
            className={`p-2 rounded shadow-sm ${c.status === "failed"
                ? "bg-red-200 text-red-900"
                : "bg-green-100 text-green-900"
              }`}
          >
            {c.device_type} - {c.action} - {c.status}
          </div>
        ))}
      </div>
    </Card>
  );
}
