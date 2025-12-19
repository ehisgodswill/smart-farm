import { UserRole } from "./enums";

export interface User {
  id: string;
  username: string;
  email: string;
  role: UserRole;
  created_at: string;
}
