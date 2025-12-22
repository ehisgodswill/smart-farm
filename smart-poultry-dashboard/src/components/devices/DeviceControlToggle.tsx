import { Switch, CircularProgress } from "@mui/material";
import { useState } from "react";
import { updateDevice } from "../../api/devices";
import { Device } from "../../types/device";
import { ActionValue } from "../../types/enums";

interface Props {
  device: Device;
  onUpdated: (device: Device) => void;
}

export default function DeviceControlToggle({ device, onUpdated }: Props) {
  const [loading, setLoading] = useState(false);

  const handleToggle = async () => {
    setLoading(true);
    const nextState = device.state === ActionValue.ON ? ActionValue.OFF : ActionValue.ON;

    try {
      const updated = await updateDevice(device.id, {
        state: nextState,
      });
      onUpdated(updated);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <CircularProgress size={20} />;

  return (
    <Switch
      checked={device.state === ActionValue.ON}
      onChange={handleToggle}
      color="success"
    />
  );
}
