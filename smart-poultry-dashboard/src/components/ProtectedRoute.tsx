import { JSX } from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";
import { UserRole } from "../types/auth";

export function ProtectedRoute({
  children,
  roles,
}: {
  children: JSX.Element;
  roles?: UserRole[];
}) {
  const { user, loading } = useAuth();

  if (loading) return null;

  if (!user) return <Navigate to="/login" replace />;

  if (roles && !roles.includes(user.role)) {
    return <Navigate to="/unauthorized" replace />;
  }

  return children;
}