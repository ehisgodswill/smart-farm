import { useState, useEffect } from "react";
import { Button } from "@mui/material";
import FarmModal from "../components/FarmModal";
import { api } from "../utils/api";
import { Farm } from "../types/farm";

export default function FarmsPage() {
  const [farms, setFarms] = useState<Farm[]>([]);
  const [loading, setLoading] = useState(false);
  const [modalOpen, setModalOpen] = useState(false);
  const [editingFarm, setEditingFarm] = useState<Farm | null>(null);

  const fetchFarms = async () => {
    try {
      const data = await api<Farm[]>("/farms");
      setFarms(data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchFarms();
  }, []);

  const handleSave = async (payload: { name: string; location: string }) => {
    setLoading(true);
    try {
      if (editingFarm) {
        const updated = await api<Farm>(`/farms/${editingFarm.id}`, {
          method: "PUT",
          body: JSON.stringify(payload),
        });
        setFarms((prev) => prev.map((f) => (f.id === updated.id ? updated : f)));
      } else {
        const created = await api<Farm>("/farms", {
          method: "POST",
          body: JSON.stringify(payload),
        });
        setFarms((prev) => [...prev, created]);
      }
      setModalOpen(false);
      setEditingFarm(null);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = (farm: Farm) => {
    setEditingFarm(farm);
    setModalOpen(true);
  };

  const handleDelete = async (farm: Farm) => {
    if (!confirm(`Delete farm "${farm.name}"?`)) return;
    try {
      await api(`/farms/${farm.id}`, { method: "DELETE" });
      setFarms((prev) => prev.filter((f) => f.id !== farm.id));
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-green-800">Farms</h2>
        <Button
          onClick={() => setModalOpen(true)}
          variant="contained"
          className="bg-green-500 hover:bg-green-600 text-yellow-100 font-bold"
        >
          New Farm
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {farms.map((farm) => (
          <div
            key={farm.id}
            className="p-4 rounded-lg shadow bg-white flex justify-between items-center"
          >
            <div>
              <h3 className="text-lg font-bold">{farm.name}</h3>
              <p className="text-gray-600">{farm.location}</p>
            </div>
            <div className="flex gap-2">
              <Button
                onClick={() => handleEdit(farm)}
                size="small"
                className="bg-yellow-300 hover:bg-yellow-400 text-green-900 font-bold"
              >
                Edit
              </Button>
              <Button
                onClick={() => handleDelete(farm)}
                size="small"
                className="bg-red-500 hover:bg-red-600 text-white font-bold"
              >
                Delete
              </Button>
            </div>
          </div>
        ))}
      </div>

      <FarmModal
        open={modalOpen}
        onClose={() => {
          setModalOpen(false);
          setEditingFarm(null);
        }}
        onSave={handleSave}
        initialData={editingFarm || undefined}
        loading={loading}
      />
    </div>
  );
}
