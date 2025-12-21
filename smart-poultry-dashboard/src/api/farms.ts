import { api } from "../utils/api";
import { Farm, FarmCreate, FarmUpdate } from "../types/farm";

export const listFarms = () => api<Farm[]>("/farms");

export const getFarm = (id: string) =>
  api<Farm>(`/farms/${id}`);

export const createFarm = (data: FarmCreate) =>
  api<Farm>("/farms", {
    method: "POST",
    body: JSON.stringify(data),
  });

export const updateFarm = (id: string, data: FarmUpdate) =>
  api<Farm>(`/farms/${id}`, {
    method: "PUT",
    body: JSON.stringify(data),
  });

export const deleteFarm = (id: string) =>
  api<Farm>(`/farms/${id}`, { method: "DELETE" });
