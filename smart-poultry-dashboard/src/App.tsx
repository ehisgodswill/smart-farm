import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import Dashboard from "./pages/Dashboard";
import RequireAuth from "./components/RequireAuth";
import FarmsPage from "./pages/FarmsPage";
import PensPage from "./pages/PensPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <RequireAuth>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/farms" element={<FarmsPage />} />
            <Route path="/pens" element={<PensPage />} />
            {/* Add more pages: Devices, Sensors, Rules, VisionEvents */}
          </Routes>
        </RequireAuth>
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
