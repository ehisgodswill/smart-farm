import { useEffect } from "react";
import { wsClient } from "../utils/ws";
import { DeviceCommand } from "../types/deviceCommand";
import { queryClient } from "../utils/queryClient";

export const useLiveDeviceCommands = () => {
  useEffect(() => {
    wsClient.connect();

    const unsubscribe = wsClient.subscribe((event) => {
      if (event.type !== "device_command") return;

      queryClient.setQueryData<DeviceCommand[]>(
        ["device-commands"],
        (old = []) => [event.payload, ...old]
      );
    });

    return unsubscribe;
  }, []);
};
