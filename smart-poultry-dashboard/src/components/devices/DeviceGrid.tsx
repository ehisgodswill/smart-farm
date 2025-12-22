import { Device } from "../../types/device";
import DeviceCard from "./DeviceCard";

interface Props {
  devices: Device[];
  onUpdated: (device: Device) => void;
}

export default function DeviceGrid({ devices, onUpdated }: Props) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
      {devices.map((d) => (
        <DeviceCard key={d.id} device={d} onUpdated={onUpdated} />
      ))}
    </div>
  );
}
