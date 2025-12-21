import { useQuery, useMutation } from "@tanstack/react-query";
import * as api from "../api/farms";
import { queryClient } from "../utils/queryClient";

export const useFarms = () =>
  useQuery({
    queryKey: ["farms"],
    queryFn: api.listFarms,
  });

export const useCreateFarm = () =>
  useMutation({
    mutationFn: api.createFarm,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["farms"] });
    },
  });
