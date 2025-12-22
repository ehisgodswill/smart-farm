import { BrowserRouter, Routes, Route, Navigate, Outlet } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import Dashboard from "./pages/Dashboard";
import FarmsPage from "./pages/FarmsPage";
import PensPage from "./pages/PensPage";
import { AuthProvider } from "./context/AuthContext";
import { ProtectedRoute } from "./components/ProtectedRoute";
import Layout from "./components/Layout";
import RegisterPage from "./pages/RegisterPage";
import DevicesPage from "./pages/DevicesPage";

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />

          <Route path="/" element={
            <ProtectedRoute>
              <Layout><Outlet /></Layout>
            </ProtectedRoute>}>
            <Route index element={<Dashboard />} />
            <Route path="/devices" element={<DevicesPage />} />
            <Route path="/farms" element={<FarmsPage />} />
            <Route path="/pens" element={<PensPage />} />


            <Route
              path="admin"
              element={
                <ProtectedRoute roles={["ADMIN"]}>
                  <></>
                  {/* <AdminPage /> */}
                </ProtectedRoute>
              }
            />
            {/* Add more protected routes here */}
          </Route>

          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;