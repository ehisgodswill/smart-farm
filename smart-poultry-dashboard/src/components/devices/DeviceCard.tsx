import { Card, Typography, Chip } from "@mui/material";
import DeviceControlToggle from "./DeviceControlToggle";
import { Device } from "../../types/device";
import { ActionValue } from "../../types/enums";

interface Props {
  device: Device;
  onUpdated: (device: Device) => void;
}

export default function DeviceCard({ device, onUpdated }: Props) {
  return (
    <Card className="p-5 shadow-lg border-l-4 border-green-500 bg-gradient-to-br from-green-50 to-yellow-50">
      <div className="flex justify-between items-center">
        <Typography variant="h6" className="font-bold">
          {device.type}
        </Typography>

        <Chip
          label={device.state}
          color={device.state === ActionValue.ON ? "success" : "default"}
        />
      </div>

      <Typography variant="body2" className="text-gray-600 mt-1">
        Pen ID: {device.pen_id}
      </Typography>

      {device.last_command_at && (
        <Typography variant="caption" className="text-gray-500">
          Last command: {new Date(device.last_command_at).toLocaleString()}
        </Typography>
      )}

      <div className="mt-4 flex justify-end">
        <DeviceControlToggle device={device} onUpdated={onUpdated} />
      </div>
    </Card>
  );
}
