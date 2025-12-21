import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import {
  Button,
  TextField,
  Card,
  Typography,
  MenuItem,
  CircularProgress,
} from "@mui/material";
import { AuthAPI } from "../api/auth";

export default function RegisterPage() {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("MANAGER");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      await AuthAPI.register({
        username,
        email,
        password,
        role,
      });
      navigate("/login");
    } catch {
      setError("Registration failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="h-screen flex items-center justify-center bg-gradient-to-br from-green-500 via-green-400 to-yellow-300">
      <Card className="p-8 w-[420px] shadow-xl rounded-xl">
        <Typography
          variant="h5"
          className="mb-6 text-center font-bold text-green-800"
        >
          Create Account
        </Typography>

        {error && (
          <Typography color="error" className="mb-3 text-sm text-center">
            {error}
          </Typography>
        )}

        <form className="flex flex-col gap-5" onSubmit={handleSubmit}>
          <TextField
            label="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            disabled={loading}
          />

          <TextField
            label="Email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            disabled={loading}
          />

          <TextField
            label="Password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            disabled={loading}
          />

          <TextField
            select
            label="Role"
            value={role}
            onChange={(e) => setRole(e.target.value)}
            disabled={loading}
          >
            {/* <MenuItem value="ADMIN">Admin</MenuItem> */}
            <MenuItem value="FARM_MANAGER">Manager</MenuItem>
            <MenuItem value="STAFF">Staff</MenuItem>
          </TextField>

          <Button
            type="submit"
            variant="contained"
            fullWidth
            disabled={loading}
            className="bg-green-600 hover:bg-green-700"
          >
            {loading ? <CircularProgress size={22} /> : "Register"}
          </Button>
        </form>

        <Typography className="mt-4 text-center text-sm text-gray-600">
          Already have an account?{" "}
          <Link to="/login" className="text-green-700 font-medium">
            Login
          </Link>
        </Typography>
      </Card>
    </div>
  );
}
