import { api } from "./client";
import { Rule, RuleCreate, RuleUpdate } from "../types/rule";

export const listRules = () => api<Rule[]>("/rules");

export const createRule = (data: RuleCreate) =>
  api<Rule>("/rules", {
    method: "POST",
    body: JSON.stringify(data),
  });

export const updateRule = (id: string, data: RuleUpdate) =>
  api<Rule>(`/rules/${id}`, {
    method: "PUT",
    body: JSON.stringify(data),
  });

export const deleteRule = (id: string) =>
  api<Rule>(`/rules/${id}`, { method: "DELETE" });
