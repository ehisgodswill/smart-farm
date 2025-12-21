import { useQuery } from "@tanstack/react-query";
import { api } from "../utils/api";
import { DeviceCommand } from "../types/deviceCommand";

export const useDeviceCommands = (penId: string) => {
  return useQuery<DeviceCommand[]>({
    queryKey: ["device-commands", penId],
    queryFn: () =>
      api<DeviceCommand[]>(
        `/device-commands?pen_id=${penId}&limit=50`
      ),
    refetchInterval: 60_000,
    enabled: !!penId,
  });
}
