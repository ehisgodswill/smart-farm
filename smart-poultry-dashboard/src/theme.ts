import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      main: "#4CAF50", // green
    },
    secondary: {
      main: "#FFEB3B", // yellow
    },
    background: {
      default: "#f4f9f4",
    },
  },
  typography: {
    fontFamily: "'Inter', sans-serif",
  },
});

export default theme;
