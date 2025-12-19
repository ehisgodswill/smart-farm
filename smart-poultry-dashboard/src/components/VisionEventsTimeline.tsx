interface VisionEvent {
  id: string;
  pen_id: string;
  bird_id?: string;
  type: string; // sick, aggression, abnormal_behavior
  confidence?: number;
  image_url?: string;
  timestamp: string;
}

interface VisionEventsTimelineProps {
  events: VisionEvent[];
}

export function VisionEventsTimeline({ events }: VisionEventsTimelineProps) {
  return (
    <div className="bg-gray-800 text-white p-4 rounded shadow-md">
      <h3 className="text-lg font-bold mb-2">Vision Events</h3>
      <ul className="space-y-2 max-h-96 overflow-y-auto">
        {events.map((event) => (
          <li key={event.id} className="flex items-center space-x-2 border-b border-gray-700 pb-1">
            <span
              className={`px-2 py-1 rounded ${event.type === "sick" ? "bg-red-500" :
                  event.type === "aggression" ? "bg-yellow-500" :
                    "bg-blue-500"
                } text-xs font-bold`}
            >
              {event.type.toUpperCase()}
            </span>
            <span className="flex-1 text-sm">
              Pen: {event.pen_id} {event.bird_id ? `| Bird: ${event.bird_id}` : ""}
            </span>
            <span className="text-xs text-gray-400">{new Date(event.timestamp).toLocaleTimeString()}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
