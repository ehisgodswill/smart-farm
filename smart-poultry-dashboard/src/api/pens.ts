import { api } from "./client";
import { Pen, PenCreate, PenUpdate } from "../types/pen";

export const listPens = () => api<Pen[]>("/pens");

export const getPen = (id: string) =>
  api<Pen>(`/pens/${id}`);

export const createPen = (data: PenCreate) =>
  api<Pen>("/pens", {
    method: "POST",
    body: JSON.stringify(data),
  });

export const updatePen = (id: string, data: PenUpdate) =>
  api<Pen>(`/pens/${id}`, {
    method: "PUT",
    body: JSON.stringify(data),
  });

export const deletePen = (id: string) =>
  api<Pen>(`/pens/${id}`, { method: "DELETE" });
