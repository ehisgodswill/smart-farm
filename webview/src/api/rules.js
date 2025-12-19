const API_BASE = "http://localhost:8000/api/rules";

export async function fetchRules () {
  const res = await fetch(API_BASE);
  return res.json();
}

export async function createRule (rule) {
  const res = await fetch(API_BASE, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(rule),
  });
  return res.json();
}

export async function updateRule (rule_id, updates) {
  const res = await fetch(`${API_BASE}/${rule_id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(updates),
  });
  return res.json();
}
