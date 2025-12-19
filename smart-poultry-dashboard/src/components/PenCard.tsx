import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

interface SensorReading {
  type: string;
  value: number;
  timestamp: string;
}

interface PenCardProps {
  name: string;
  readings: SensorReading[];
  devices: { type: string; state: string }[];
}

export function PenCard({ name, readings, devices }: PenCardProps) {
  return (
    <div className="bg-gray-800 text-white p-4 rounded shadow-md">
      <h3 className="text-xl font-bold">{name}</h3>

      <div className="h-32 mt-2">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={readings}>
            <XAxis dataKey="timestamp" hide />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="value" stroke="#4ade80" />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="mt-2 flex space-x-2">
        {devices.map((d) => (
          <span
            key={d.type}
            className={`px-2 py-1 rounded ${d.state === "ON" ? "bg-green-500" : "bg-red-500"
              }`}
          >
            {d.type}
          </span>
        ))}
      </div>
    </div>
  );
}
