import { useEffect } from "react";
import { wsClient } from "../helper/ws";
import { DeviceCommand } from "../types/deviceCommand";
import { queryClient } from "../helper/queryClient";

export const useLiveDeviceCommands = () => {
  useEffect(() => {
    wsClient.connect();

    const unsub = wsClient.subscribe((event) => {
      if (event.type !== "device_command") return;

      queryClient.setQueryData<DeviceCommand[]>(
        ["device-commands"],
        (old = []) => [event.payload, ...old]
      );
    });

    return unsub;
  }, []);
};
