import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  TextField
} from "@mui/material";
import { useState, useEffect } from "react";
import { Farm } from "../types/farm";

interface Props {
  open: boolean;
  onClose: () => void;
  onSave: (data: { name: string; location: string }) => void;
  initialData?: Farm;
  loading?: boolean;
}

export default function FarmModal({ open, onClose, onSave, initialData, loading = false }: Props) {
  const [name, setName] = useState("");
  const [location, setLocation] = useState("");

  useEffect(() => {
    if (open) {
      if (initialData) {
        // eslint-disable-next-line react-hooks/set-state-in-effect
        setName(initialData.name);
        setLocation(initialData.location || "");
      } else {
        setName("");
        setLocation("");
      }
    }
  }, [open, initialData]);

  const handleSubmit = (e?: React.FormEvent) => {
    e?.preventDefault();
    if (name.trim() && location.trim()) {
      onSave({ name: name.trim(), location: location.trim() });
    }
  };

  const isValid = name.trim().length > 0 && location.trim().length > 0;

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <form onSubmit={handleSubmit}>
        <DialogTitle>{initialData ? "Edit Farm" : "New Farm"}</DialogTitle>
        <DialogContent className="flex flex-col gap-4 mt-2">
          <TextField
            label="Farm Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            fullWidth
            required
            autoFocus
            disabled={loading}
            error={name.length > 0 && name.trim().length === 0}
            helperText={name.length > 0 && name.trim().length === 0 ? "Farm name is required" : ""}
          />
          <TextField
            label="Location"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            fullWidth
            required
            disabled={loading}
            error={location.length > 0 && location.trim().length === 0}
            helperText={location.length > 0 && location.trim().length === 0 ? "Location is required" : ""}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={onClose} color="secondary" disabled={loading}>
            Cancel
          </Button>
          <Button
            onClick={handleSubmit}
            type="submit"
            color="primary"
            variant="contained"
            disabled={!isValid || loading}
          >
            {loading ? "Saving..." : initialData ? "Update" : "Create"}
          </Button>
        </DialogActions>
      </form>
    </Dialog>
  );
}