import { api } from "../utils/api";
import { LoginResponse, User } from "../types/auth";

export const AuthAPI = {
  login: (username: string, password: string) =>
    api<LoginResponse>("/auth/login", {
      method: "POST",
      body: JSON.stringify({ username, password }),
    }),

  register: (data: {
    username: string;
    email: string;
    password: string;
    role: string;
  }) =>
    api<User>("/auth/register", {
      method: "POST",
      body: JSON.stringify(data),
    }),

  me: () => api<User>("/auth/me"),

  refresh: (refresh_token: string) =>
    api<LoginResponse>("/auth/refresh", {
      method: "POST",
      body: JSON.stringify({ refresh_token }),
    }),
};
