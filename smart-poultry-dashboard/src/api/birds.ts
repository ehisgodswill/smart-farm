import { api } from "./client";
import { Bird, BirdCreate, BirdUpdate } from "../types/bird";

export const listBirds = (penId?: string) =>
  api<Bird[]>(penId ? `/birds?pen_id=${penId}` : "/birds");

export const getBird = (id: string) =>
  api<Bird>(`/birds/${id}`);

export const createBird = (data: BirdCreate) =>
  api<Bird>("/birds", {
    method: "POST",
    body: JSON.stringify(data),
  });

export const updateBird = (id: string, data: BirdUpdate) =>
  api<Bird>(`/birds/${id}`, {
    method: "PUT",
    body: JSON.stringify(data),
  });

export const deleteBird = (id: string) =>
  api<Bird>(`/birds/${id}`, { method: "DELETE" });
