import { VisionEvent } from "../types/visionEvent";

interface Props {
  events: VisionEvent[];
}

const severityColor: Record<string, string> = {
  sick: "red",
  abnormal_behavior: "orange",
  aggression: "purple",
};

export function AlertsPanel({ events }: Props) {
  if (!events.length) {
    return <div>No alerts</div>;
  }

  return (
    <div style={{ marginTop: 24 }}>
      <h4>Alerts</h4>

      <ul>
        {events.slice(0, 10).map((e) => (
          <li key={e.id} style={{ color: severityColor[e.type] || "black" }}>
            <strong>{e.type.replace("_", " ")}</strong>{" "}
            ({Math.round((e.confidence ?? 0) * 100)}%) –{" "}
            {new Date(e.timestamp).toLocaleTimeString()}
          </li>
        ))}
      </ul>
    </div>
  );
}
