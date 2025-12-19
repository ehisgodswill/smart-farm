import { useEffect } from "react";
import { wsClient } from "../helper/ws";
import { VisionEvent } from "../types/visionEvent";
import { queryClient } from "../helper/queryClient";

export const useLiveVisionEvents = () => {
  useEffect(() => {
    wsClient.connect();

    const unsub = wsClient.subscribe((event) => {
      if (event.type !== "vision_event") return;

      queryClient.setQueryData<VisionEvent[]>(
        ["vision-events"],
        (old = []) => [event.payload, ...old]
      );
    });

    return unsub;
  }, []);
};
