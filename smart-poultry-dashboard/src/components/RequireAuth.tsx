import { Navigate, Outlet } from "react-router-dom";
import Layout from "./Layout";

export default function RequireAuth() {
  const token = localStorage.getItem("token");
  if (token) return <Navigate to="/login" />;

  return <Layout><Outlet /></Layout>;
}
