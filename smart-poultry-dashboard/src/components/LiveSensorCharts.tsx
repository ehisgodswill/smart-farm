import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";
import { SensorReading } from "../types/sensorReading";

interface Props {
  readings: SensorReading[];
  label: string;
  unit: string;
}

export function LiveSensorChart({ readings, label, unit }: Props) {
  const data = [...readings]
    .slice(0, 50)
    .reverse()
    .map((r) => ({
      time: new Date(r.timestamp).toLocaleTimeString(),
      value: r.value,
    }));

  return (
    <div style={{ marginBottom: 24 }}>
      <h4>{label}</h4>

      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis unit={unit} />
          <Tooltip />
          <Line
            type="monotone"
            dataKey="value"
            stroke="#3b82f6"
            strokeWidth={2}
            dot={false}
            isAnimationActive={false}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
