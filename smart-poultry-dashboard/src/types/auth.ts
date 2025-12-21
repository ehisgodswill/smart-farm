export type UserRole = "ADMIN" | "MANAGER" | "VIEWER";

export interface User {
  id: string;
  username: string;
  email: string;
  role: UserRole;
}

export interface LoginResponse {
  access_token: string;
  refresh_token: string;
}

export interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
}
