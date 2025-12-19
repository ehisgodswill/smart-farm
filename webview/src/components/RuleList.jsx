import { useState, useEffect } from "react";
import { fetchRules, updateRule } from "../api/rules";
import RuleRow from "./RuleRow";

export default function RuleList () {
  const [rules, setRules] = useState([]);

  useEffect(() => {
    loadRules();
  }, []);

  async function loadRules () {
    const data = await fetchRules();
    setRules(data);
  }

  async function toggleEnabled (rule_id, enabled) {
    await updateRule(rule_id, { enabled });
    loadRules();
  }

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Automation Rules</h2>
      <table className="w-full table-auto border">
        <thead>
          <tr>
            <th>Pen</th>
            <th>Sensor</th>
            <th>Operator</th>
            <th>Threshold</th>
            <th>Device</th>
            <th>Action</th>
            <th>Enabled</th>
          </tr>
        </thead>
        <tbody>
          {rules.map(rule => (
            <RuleRow key={rule.id} rule={rule} toggleEnabled={toggleEnabled} />
          ))}
        </tbody>
      </table>
    </div>
  );
}
