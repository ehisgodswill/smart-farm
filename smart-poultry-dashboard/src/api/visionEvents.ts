import { api } from "./client";
import { VisionEvent } from "../types/visionEvent";

export const listVisionEvents = (limit = 50) =>
  api<VisionEvent[]>(`/vision-events?limit=${limit}`);
