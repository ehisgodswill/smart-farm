import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../utils/api";
import { Button, TextField, Card, Typography } from "@mui/material";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    try {
      const data = await api<{ token: string }>("/auth/login", {
        method: "POST",
        body: JSON.stringify({ username, password }),
      });

      localStorage.setItem("token", data.token);
      navigate("/");
    } catch {
      setError("Login failed");
    }
  };

  return (
    <div className="h-screen flex items-center justify-center bg-gradient-to-r from-green-400 to-yellow-300">
      <Card className="p-8 w-96 shadow-lg">
        <Typography variant="h5" className="mb-6 text-center font-bold">
          Smart Poultry Login
        </Typography>

        {error && <Typography color="error">{error}</Typography>}

        <form className="flex flex-col gap-4" onSubmit={handleSubmit}>
          <TextField
            label="Username"
            variant="outlined"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            fullWidth
            required
          />
          <TextField
            label="Password"
            variant="outlined"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            fullWidth
            required
          />
          <Button type="submit" variant="contained" color="primary" fullWidth>
            Login
          </Button>
        </form>
      </Card>
    </div>
  );
}
