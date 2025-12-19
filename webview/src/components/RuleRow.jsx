export default function RuleRow ({ rule, toggleEnabled }) {
  const [sensor_type, operator, threshold] = rule.condition.split(" ");
  const [action_device, action_value] = rule.action.split(":");

  return (
    <tr className="border">
      <td className="p-2">{rule.pen_id || "All"}</td>
      <td className="p-2">{sensor_type}</td>
      <td className="p-2">{operator}</td>
      <td className="p-2">{threshold}</td>
      <td className="p-2">{action_device}</td>
      <td className="p-2">{action_value}</td>
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
