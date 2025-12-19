import { useState } from "react";
import { createRule } from "../api/rules";

export default function RuleForm ({ onSaved }) {
  const [form, setForm] = useState({
    name: "",
    pen_id: "",
    sensor_type: "temperature",
    operator: ">",
    threshold: 30,
    action_device: "fan",
    action_value: "ON",
    enabled: true
  });

  function handleChange (e) {
    const { name, value, type, checked } = e.target;
    setForm({
      ...form,
      [name]: type === "checkbox" ? checked : value
    });
  }

  async function handleSubmit (e) {
    e.preventDefault();

    const payload = {
      name: form.name,
      pen_id: form.pen_id || null,
      condition: `${form.sensor_type} ${form.operator} ${form.threshold}`,
      action: `${form.action_device}:${form.action_value}`,
      enabled: form.enabled
    };

    await createRule(payload);
    onSaved();
  }

  return (
    <form onSubmit={handleSubmit} className="p-4 border mb-4">

      <div className="flex gap-5 mb-4">
        <label>Rule Name</label>
        <input
          name="name"
          value={form.name}
          onChange={handleChange}
          required
        />
      </div>

      <div className="flex gap-5 mb-4">
        <label>Pen ID (leave blank = global)</label>
        <input
          name="pen_id"
          value={form.pen_id}
          onChange={handleChange}
        />
      </div>

      <div className="flex gap-5 mb-4">
        <label>Sensor Type</label>
        <select
          name="sensor_type"
          value={form.sensor_type}
          onChange={handleChange}
        >
          <option value="temperature">Temperature</option>
          <option value="humidity">Humidity</option>
        </select>
      </div>

      <div className="flex gap-5 mb-4">
        <label>Operator</label>
        <select
          name="operator"
          value={form.operator}
          onChange={handleChange}
        >
          <option value=">">{">"}</option>
          <option value="<">{"<"}</option>
          <option value=">=">{">="}</option>
          <option value="<=">{"<="}</option>
        </select>
      </div>

      <div className="flex gap-5 mb-4">
        <label>Threshold</label>
        <input
          type="number"
          name="threshold"
          value={form.threshold}
          onChange={handleChange}
        />
      </div>

      <div className="flex gap-5 mb-4">
        <label>Device</label>
        <input
          name="action_device"
          value={form.action_device}
          onChange={handleChange}
        />
      </div>

      <div className="flex gap-5 mb-4">
        <label>Action</label>
        <select
          name="action_value"
          value={form.action_value}
          onChange={handleChange}
        >
          <option value="ON">ON</option>
          <option value="OFF">OFF</option>
        </select>
      </div>

      <div className="flex gap-5 mb-4">
        <label>
          <input
            type="checkbox"
            name="enabled"
            checked={form.enabled}
            onChange={handleChange}
          />
          Enabled
        </label>
      </div>

      <button type="submit" className="mt-2 p-2 bg-blue-500 text-white">
        Save Rule
      </button>
    </form>
  );
}
