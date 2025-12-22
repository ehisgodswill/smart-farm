import { useState, useEffect } from "react";
import { Button } from "@mui/material";
import PenModal from "../components/PenModal";
import { api } from "../utils/api";
import { Pen } from "../types/pen";

export default function PensPage() {
  const [pens, setPens] = useState<Pen[]>([]);
  const [loading, setLoading] = useState(false);
  const [modalOpen, setModalOpen] = useState(false);
  const [editingPen, setEditingPen] = useState<Pen | null>(null);

  const fetchPens = async () => {
    try {
      const data = await api<Pen[]>("/pens");
      setPens(data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchPens();
  }, []);

  const handleSave = async (payload: { name: string; capacity: number; farm_id: string }) => {
    setLoading(true);
    try {
      if (editingPen) {
        const updated = await api<Pen>(`/pens/${editingPen.id}`, {
          method: "PUT",
          body: JSON.stringify(payload),
        });
        setPens((prev) => prev.map((p) => (p.id === updated.id ? updated : p)));
      } else {
        const created = await api<Pen>("/pens", {
          method: "POST",
          body: JSON.stringify(payload),
        });
        setPens((prev) => [...prev, created]);
      }
      setModalOpen(false);
      setEditingPen(null);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = (pen: Pen) => {
    setEditingPen(pen);
    setModalOpen(true);
  };

  const handleDelete = async (pen: Pen) => {
    if (!confirm(`Delete pen "${pen.name}"?`)) return;
    try {
      await api(`/pens/${pen.id}`, { method: "DELETE" });
      setPens((prev) => prev.filter((p) => p.id !== pen.id));
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-green-800">Pens</h2>
        <Button
          onClick={() => setModalOpen(true)}
          variant="contained"
          className="bg-green-500 hover:bg-green-600 text-yellow-100 font-bold"
        >
          New Pen
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {pens.map((pen) => (
          <div
            key={pen.id}
            className="p-4 rounded-lg shadow bg-white flex justify-between items-center"
          >
            <div>
              <h3 className="text-lg font-bold">{pen.name}</h3>
              <p className="text-gray-600">Capacity: {pen.capacity}</p>
              {/* <p className="text-gray-600">Farm ID: {pen.farm_id}</p> */}
            </div>
            <div className="flex gap-2">
              <Button
                onClick={() => handleEdit(pen)}
                size="small"
                className="bg-yellow-300 hover:bg-yellow-400 text-green-900 font-bold"
              >
                Edit
              </Button>
              <Button
                onClick={() => handleDelete(pen)}
                size="small"
                className="bg-red-500 hover:bg-red-600 text-white font-bold"
              >
                Delete
              </Button>
            </div>
          </div>
        ))}
      </div>

      <PenModal
        open={modalOpen}
        onClose={() => {
          setModalOpen(false);
          setEditingPen(null);
        }}
        onSave={handleSave}
        initialData={editingPen || undefined}
        loading={loading}
      />
    </div>
  );
}
