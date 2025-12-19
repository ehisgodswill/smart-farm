import { api } from "./client";
import { User } from "../types/user";

export const listUsers = () => api<User[]>("/users");
