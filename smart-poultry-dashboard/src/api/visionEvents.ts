import { api } from "../utils/api";
import { VisionEvent } from "../types/visionEvent";

export const listVisionEvents = (limit = 50) =>
  api<VisionEvent[]>(`/vision-events?limit=${limit}`);
