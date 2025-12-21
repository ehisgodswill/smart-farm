import { AppBar, Toolbar, Typography } from "@mui/material";

export default function TopNav() {
  return (
    <AppBar position="fixed" className="bg-gradient-to-r from-green-400 to-yellow-300">
      <Toolbar>
        <Typography variant="h6" className="flex-1">
          Smart Poultry Dashboard
        </Typography>
        <div className="flex gap-4">
          {/* Placeholder for user info, notifications */}
          <Typography>User</Typography>
        </div>
      </Toolbar>
    </AppBar>
  );
}
