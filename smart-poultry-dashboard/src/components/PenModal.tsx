import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  TextField,
  MenuItem
} from "@mui/material";
import { useState, useEffect } from "react";
import { api } from "../utils/api";
import { Farm } from "../types/farm";
import { Pen } from "../types/pen";

interface Props {
  open: boolean;
  onClose: () => void;
  onSave: (data: { name: string; capacity: number; farm_id: string }) => void;
  initialData?: Pen;
  loading?: boolean;
}

export default function PenModal({ open, onClose, onSave, initialData, loading = false }: Props) {
  const [name, setName] = useState("");
  const [capacity, setCapacity] = useState<string>("");
  const [farmId, setFarmId] = useState<string>("");
  const [farms, setFarms] = useState<Farm[]>([]);
  const [loadingFarms, setLoadingFarms] = useState(false);

  useEffect(() => {
    if (open) {
      fetchFarms();

      if (initialData) {
        setName(initialData.name);
        setCapacity(initialData.capacity?.toString() || "");
        setFarmId(initialData.farm_id);
      } else {
        setName("");
        setCapacity("");
        setFarmId("");
      }
    }
  }, [open, initialData]);

  const fetchFarms = async () => {
    setLoadingFarms(true);
    try {
      const data = await api<Farm[]>("/farms");
      setFarms(data);
    } catch (err) {
      console.error("Failed to fetch farms:", err);
    } finally {
      setLoadingFarms(false);
    }
  };

  const handleSubmit = (e?: React.FormEvent) => {
    e?.preventDefault();
    const capacityNum = parseInt(capacity, 10);

    if (name.trim() && !isNaN(capacityNum) && capacityNum > 0 && farmId) {
      onSave({
        name: name.trim(),
        capacity: capacityNum,
        farm_id: farmId
      });
    }
  };

  const capacityNum = parseInt(capacity, 10);
  const isCapacityValid = capacity !== "" && !isNaN(capacityNum) && capacityNum > 0;
  const isValid = name.trim().length > 0 && isCapacityValid && farmId !== "";

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <form onSubmit={handleSubmit}>
        <DialogTitle>{initialData ? "Edit Pen" : "New Pen"}</DialogTitle>
        <DialogContent className="flex flex-col gap-4 mt-2">
          <TextField
            label="Pen Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            fullWidth
            required
            autoFocus
            disabled={loading}
            error={name.length > 0 && name.trim().length === 0}
            helperText={name.length > 0 && name.trim().length === 0 ? "Pen name is required" : ""}
          />

          <TextField
            label="Capacity"
            type="number"
            value={capacity}
            onChange={(e) => setCapacity(e.target.value)}
            fullWidth
            required
            disabled={loading}
            inputProps={{
              min: 1,
              step: 1
            }}
            error={capacity !== "" && !isCapacityValid}
            helperText={
              capacity !== "" && !isCapacityValid
                ? "Capacity must be a positive number"
                : "Number of birds this pen can hold"
            }
          />

          <TextField
            select
            label="Farm"
            value={farmId}
            onChange={(e) => setFarmId(e.target.value)}
            fullWidth
            required
            disabled={loading || loadingFarms}
            error={farmId === "" && !loadingFarms}
            helperText={loadingFarms ? "Loading farms..." : "Select the farm for this pen"}
          >
            {farms.length === 0 && !loadingFarms && (
              <MenuItem value="" disabled>
                No farms available
              </MenuItem>
            )}
            {farms.map((farm) => (
              <MenuItem key={farm.id} value={farm.id}>
                {farm.name}
              </MenuItem>
            ))}
          </TextField>
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
            disabled={!isValid || loading || loadingFarms}
          >
            {loading ? "Saving..." : initialData ? "Update" : "Create"}
          </Button>
        </DialogActions>
      </form>
    </Dialog>
  );
}