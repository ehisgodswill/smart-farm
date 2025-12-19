export interface Pen {
  id: string;
  farm_id: string;
  name: string;
  capacity?: number | null;
  created_at: string;
}

export interface PenCreate {
  farm_id: string;
  name: string;
  capacity?: number | null;
}

export interface PenUpdate {
  name?: string;
  capacity?: number | null;
}
