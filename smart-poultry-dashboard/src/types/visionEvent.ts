export type VisionEventType =
  | "sick"
  | "aggression"
  | "abnormal_behavior"
  | "inactivity";

export interface VisionEvent {
  id: string;
  pen_id: string;
  bird_id?: string | null;
  type: VisionEventType;
  confidence?: number | null;
  image_url?: string | null;
  timestamp: string;
}
