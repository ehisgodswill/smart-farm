const API_BASE = "http://localhost:8000/api";

export async function fetchPens() {
  const res = await fetch(`${API_BASE}/pens`);
  return res.json();
}

export async function fetchDevices() {
  const res = await fetch(`${API_BASE}/devices`);
  return res.json();
}

export async function fetchDeviceCommands() {
  const res = await fetch(`${API_BASE}/device-commands?limit=50`);
  return res.json();
}

export async function fetchVisionEvents() {
  const res = await fetch(`${API_BASE}/vision-events?limit=50`);
  return res.json();
}
