import { useQuery } from "@tanstack/react-query";
import { api } from "../utils/api";
import { VisionEvent } from "../types/visionEvent";

export const useVisionEvents =(penId: string) => {
  return useQuery<VisionEvent[]>({
    queryKey: ["vision-events", penId],
    queryFn: () =>
      api<VisionEvent[]>(
        `/vision-events?pen_id=${penId}&limit=50`
      ),
    refetchInterval: 60_000,
    enabled: !!penId,
  });
}
