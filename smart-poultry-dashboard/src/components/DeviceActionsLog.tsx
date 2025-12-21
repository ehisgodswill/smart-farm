import { DeviceCommand } from "../types/deviceCommand";

interface Props {
  commands: DeviceCommand[];
}

export function DeviceActionsLog({ commands }: Props) {
  return (
    <div style={{ marginTop: 24 }}>
      <h4>Device Actions</h4>

      <ul>
        {commands.slice(0, 10).map((cmd) => (
          <li key={cmd.id}>
            [{cmd.device_type}] {cmd.action} –{" "}
            <strong>{cmd.status}</strong> @{" "}
            {new Date(cmd.created_at).toLocaleTimeString()}
          </li>
        ))}
      </ul>
    </div>
  );
}
