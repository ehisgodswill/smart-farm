import {
  useEffect,
  useState,
} from "react";
import { AuthAPI } from "../api/auth";
import { User } from "../types/auth";
import { AuthContext } from "../hooks/useAuth";

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  const login = async (username: string, password: string) => {
    const { access_token, refresh_token } = await AuthAPI.login(
      username,
      password
    );

    localStorage.setItem("access_token", access_token);
    localStorage.setItem("refresh_token", refresh_token);

    const me = await AuthAPI.me();
    setUser(me);
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    setUser(null);
  };

  const bootstrap = async () => {
    try {
      const token = localStorage.getItem("access_token");
      if (!token) return;
      const me = await AuthAPI.me();
      setUser(me);
    } catch {
      logout();
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    bootstrap();
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <AuthContext.Provider value={{ user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
