import { api } from "../utils/api";
import { User } from "../types/user";

export const listUsers = () => api<User[]>("/users");
