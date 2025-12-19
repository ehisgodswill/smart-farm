export interface Bird {
  id: string;
  pen_id: string;
  tag_id?: string | null;
  hatch_date?: string | null;
  age_days?: number | null;
  health_score?: number | null;
  status: string;
  created_at: string;
}

export interface BirdCreate {
  pen_id: string;
  tag_id?: string | null;
  hatch_date?: string | null;
}

export interface BirdUpdate {
  tag_id?: string | null;
  health_score?: number | null;
  status?: string;
}
