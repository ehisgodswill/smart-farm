import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  TextField,
  MenuItem,
} from "@mui/material";
import { useState, useEffect } from "react";
import { createDevice } from "../../api/devices";
import { DeviceType } from "../../types/enums";

export default function DeviceCreateModal({
  open,
  onClose,
  onCreated,
  penId,
}: {
  open: boolean;
  onClose: () => void;
  onCreated: () => void;
  penId: string;
}) {
  const [type, setType] = useState<DeviceType | "">("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (open) {
      setType("");
      setError(null);
    }
  }, [open]);

  const handleCreate = async () => {
    if (!type) return;

    setLoading(true);
    setError(null);

    try {
      await createDevice({ pen_id: penId, type });
      onCreated();
      onClose();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to create device");
      console.error("Failed to create device:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>Add Device</DialogTitle>

      <DialogContent className="flex flex-col gap-4 mt-2">
        <TextField
          select
          label="Device Type"
          value={type}
          onChange={(e) => setType(e.target.value as DeviceType)}
          fullWidth
          required
          disabled={loading}
          error={!!error}
          helperText={error || "Select the type of device to add"}
        >
          {Object.entries(DeviceType).map(([key, value]) => (
            <MenuItem key={key} value={value}>
              {value}
            </MenuItem>
          ))}
        </TextField>
      </DialogContent>

      <DialogActions>
        <Button onClick={onClose} disabled={loading}>
          Cancel
        </Button>
        <Button
          variant="contained"
          color="success"
          disabled={!type || loading}
          onClick={handleCreate}
        >
          {loading ? "Creating..." : "Create"}
        </Button>
      </DialogActions>
    </Dialog>
  );
}