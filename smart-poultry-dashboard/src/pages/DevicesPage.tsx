import { useEffect, useState } from "react";
import { Button, Typography, MenuItem, TextField } from "@mui/material";
import { listDevices } from "../api/devices";
import { listPens } from "../api/pens";
import { listFarms } from "../api/farms";
import { Device } from "../types/device";
import { Pen } from "../types/pen";
import { Farm } from "../types/farm";
import DeviceGrid from "../components/devices/DeviceGrid";
import DeviceCreateModal from "../components/devices/DeviceCreateModal";

export default function DevicesPage() {
  const [devices, setDevices] = useState<Device[]>([]);
  const [pens, setPens] = useState<Pen[]>([]);
  const [farms, setFarms] = useState<Farm[]>([]);
  const [selectedPenId, setSelectedPenId] = useState<string>("");
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const [pensData, farmsData] = await Promise.all([
          listPens(),
          listFarms(),
        ]);
        setPens(pensData);
        setFarms(farmsData);

        if (pensData.length > 0) {
          setSelectedPenId(pensData[0].id);
        }
      } catch (error) {
        console.error("Failed to load data:", error);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  // Load devices when pen selection changes
  useEffect(() => {
    if (!selectedPenId) return;

    const loadDevices = async () => {
      try {
        const devicesData = await listDevices(selectedPenId);
        setDevices(devicesData);
      } catch (error) {
        console.error("Failed to load devices:", error);
        setDevices([]);
      }
    };

    loadDevices();
  }, [selectedPenId]);

  const handleDeviceCreated = async () => {
    if (!selectedPenId) return;

    try {
      const data = await listDevices(selectedPenId);
      setDevices(data);
    } catch (error) {
      console.error("Failed to reload devices:", error);
    }
  };

  const handleDeviceUpdated = (updated: Device) => {
    setDevices((prev) =>
      prev.map((d) => (d.id === updated.id ? updated : d))
    );
  };

  const handleOpenModal = () => {
    if (pens.length === 0) {
      alert("Please create a pen first before adding devices");
      return;
    }
    setOpen(true);
  };

  const getFarmName = (farmId: string | null | undefined) => {
    if (!farmId) return "Unknown Farm";
    const farm = farms.find((f) => f.id === farmId);
    return farm?.name || "Unknown Farm";
  };

  const groupedPens = pens.reduce((acc, pen) => {
    const farmId = pen.farm_id || "unknown";
    if (!acc[farmId]) {
      acc[farmId] = [];
    }
    acc[farmId].push(pen);
    return acc;
  }, {} as Record<string, Pen[]>);

  if (loading) {
    return (
      <div className="p-8">
        <Typography>Loading...</Typography>
      </div>
    );
  }

  return (
    <div className="p-8 space-y-6">
      <div className="flex flex-wrap gap-4 justify-between items-center">
        <Typography variant="h4" className="font-bold text-green-800">
          Devices
        </Typography>

        <div className="flex gap-4 items-center">
          <TextField
            select
            label="Select Pen"
            value={selectedPenId}
            onChange={(e) => setSelectedPenId(e.target.value)}
            size="small"
            sx={{ minWidth: 250 }}
            disabled={pens.length === 0}
          >
            {Object.entries(groupedPens).map(([farmId, farmPens]) => {
              const farmName = getFarmName(farmId);
              return [
                <MenuItem key={`farm-${farmId}`} disabled>
                  <Typography variant="caption" className="font-bold text-green-700">
                    {farmName}
                  </Typography>
                </MenuItem>,
                ...farmPens.map((pen) => (
                  <MenuItem key={pen.id} value={pen.id} sx={{ pl: 4 }}>
                    {pen.name}
                  </MenuItem>
                )),
              ];
            })}
          </TextField>

          <Button
            variant="contained"
            color="success"
            onClick={handleOpenModal}
            disabled={!selectedPenId}
          >
            Add Device
          </Button>
        </div>
      </div>

      {!selectedPenId ? (
        <div className="text-center py-12">
          <Typography variant="h6" color="textSecondary">
            {pens.length === 0
              ? "No pens available. Please create a pen first."
              : "Select a pen to view its devices"}
          </Typography>
        </div>
      ) : devices.length === 0 ? (
        <div className="text-center py-12">
          <Typography variant="h6" color="textSecondary">
            No devices found for this pen. Add your first device!
          </Typography>
        </div>
      ) : (
        <DeviceGrid devices={devices} onUpdated={handleDeviceUpdated} />
      )}

      {selectedPenId && (
        <DeviceCreateModal
          open={open}
          onClose={() => setOpen(false)}
          onCreated={handleDeviceCreated}
          penId={selectedPenId}
        />
      )}
    </div>
  );
}