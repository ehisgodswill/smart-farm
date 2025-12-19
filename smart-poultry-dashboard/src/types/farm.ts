export interface Farm {
  id: string;
  name: string;
  location?: string | null;
  created_at: string;
}

export interface FarmCreate {
  name: string;
  location?: string | null;
}

export interface FarmUpdate {
  name?: string;
  location?: string | null;
}
