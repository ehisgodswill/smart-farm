/* eslint-disable @typescript-eslint/no-explicit-any */
import { useEffect, useState } from "react";
import { PenCard } from "../components/PenCard";
import { VisionEventsTimeline } from "../components/VisionEventsTimeline";
import { AlertsPanel } from "../components/AlertsPanel";
import { fetchPens, fetchDevices, fetchVisionEvents } from "../api";
import { useWebSocket } from "../hooks/useWebSocket";

export function Dashboard() {
  const [pens, setPens] = useState<any[]>([]);
  const [devices, setDevices] = useState<any[]>([]);
  const [visionEvents, setVisionEvents] = useState<any[]>([]);
  const [alerts, setAlerts] = useState<any[]>([]);

  const wsMessages: any[] = useWebSocket("ws://localhost:8000/ws"); // WebSocket server for live updates

  useEffect(() => {
    fetchPens().then(setPens);
    fetchDevices().then(setDevices);
    fetchVisionEvents().then(setVisionEvents);
  }, []);

  useEffect(() => {
    // Handle live messages
    wsMessages.forEach((msg) => {
      if (msg.type === "vision_event") {
        setVisionEvents((prev) => [msg, ...prev].slice(0, 50));
        setAlerts((prev) => [{ id: msg.id, type: msg.type, message: `Event: ${msg.type} in Pen ${msg.pen_id}`, pen_id: msg.pen_id, timestamp: msg.timestamp }, ...prev].slice(0, 20));
      }
      if (msg.type === "device_command_failed") {
        setAlerts((prev) => [{ ...msg, message: `Device ${msg.device_id} failed`, timestamp: msg.timestamp }, ...prev].slice(0, 20));
      }
    });
  }, [wsMessages]);

  return (
    <div className="p-4 grid grid-cols-1 lg:grid-cols-3 gap-4">
      {/* Pens grid */}
      <div className="lg:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-4">
        {pens.map((pen) => (
          <PenCard
            key={pen.id}
            name={pen.name}
            readings={pen.readings || []}
            devices={devices.filter((d) => d.pen_id === pen.id)}
          />
        ))}
      </div>

      {/* Right side: Vision Events + Alerts */}
      <div className="space-y-4">
        <VisionEventsTimeline events={visionEvents} />
        <AlertsPanel alerts={alerts} />
      </div>
    </div>
  );
}
