import { useQuery, useMutation } from "@tanstack/react-query";
import * as api from "../api/devices";
import { queryClient } from "../utils/queryClient";

export const useDevices = (penId?: string) =>
  useQuery({
    queryKey: ["devices", penId],
    queryFn: () => api.listDevices(penId),
  });

export const useCreateDevice = () =>
  useMutation({
    mutationFn: api.createDevice,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["devices"] });
    },
  });
