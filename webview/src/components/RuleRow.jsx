export default function RuleRow ({ rule, toggleEnabled }) {
  return (
    <tr className="border">
      <td className="p-2">{rule.pen_id || "All"}</td>
      <td className="p-2">{rule.sensor_type}</td>
      <td className="p-2">{rule.operator}</td>
      <td className="p-2">{rule.threshold}</td>
      <td className="p-2">{rule.action_device}</td>
      <td className="p-2">{rule.action_value}</td>
      <td className="p-2">
        <input
          type="checkbox"
          checked={rule.enabled}
          onChange={() => toggleEnabled(rule.id, !rule.enabled)}
        />
      </td>
    </tr>
  );
}
