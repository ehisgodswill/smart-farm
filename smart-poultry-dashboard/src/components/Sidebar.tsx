import { Drawer, List, ListItemButton, ListItemText, Typography } from "@mui/material";
import { useNavigate, useLocation } from "react-router-dom";

const menuItems = [
  { label: "Dashboard", path: "/" },
  { label: "Farms", path: "/farms" },
  { label: "Pens", path: "/pens" },
  { label: "Devices", path: "/devices" },
  { label: "Sensors", path: "/sensors" },
  { label: "Rules", path: "/rules" },
  { label: "Vision Events", path: "/vision-events" },
];

export default function Sidebar() {
  const navigate = useNavigate();
  const location = useLocation();

  const isSelected = (path: string) => {
    if (path === "/") {
      return location.pathname === "/";
    }
    return location.pathname.startsWith(path);
  };

  return (
    <Drawer
      variant="permanent"
      sx={{
        width: 256,
        flexShrink: 0,
        "& .MuiDrawer-paper": {
          width: 256,
          background: "linear-gradient(to bottom, #4CAF50, #FFEB3B)",
          boxSizing: "border-box"
        },
      }}
    >
      <div className="p-4">
        <Typography variant="h6" className="font-bold text-white">
          Smart Poultry
        </Typography>
      </div>
      <List>
        {menuItems.map((item) => (
          <ListItemButton
            key={item.path}
            selected={isSelected(item.path)}
            onClick={() => navigate(item.path)}
            sx={{
              color: "white",
              "&.Mui-selected": {
                backgroundColor: "rgba(255, 255, 255, 0.2)",
              },
              "&:hover": {
                backgroundColor: "rgba(255, 255, 255, 0.1)",
              },
            }}
          >
            <ListItemText primary={item.label} />
          </ListItemButton>
        ))}
      </List>
    </Drawer>
  );
}