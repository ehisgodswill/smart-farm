export type AlertLevel = "ok" | "warning" | "critical";

export interface PenStatus {
  penId: string;
  level: AlertLevel;
  reasons: string[];
}
