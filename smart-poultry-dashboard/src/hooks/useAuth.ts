import { createContext, useContext } from "react";
import { AuthContextType } from "../types/auth";


export const AuthContext = createContext<AuthContextType | null>(null);

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("AuthContext missing");
  return ctx;
};
