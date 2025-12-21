import { useQuery, useMutation } from "@tanstack/react-query";
import * as api from "../api/pens";
import { queryClient } from "../utils/queryClient";

export const usePens = () =>
  useQuery({
    queryKey: ["pens"],
    queryFn: api.listPens,
  });

export const usePensByFarm = (farmId: string) =>
  useQuery({
    queryKey: ["pens", farmId],
    queryFn: api.listPens,
    enabled: !!farmId,
  });

export const useCreatePen = () =>
  useMutation({
    mutationFn: api.createPen,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["pens"] });
    },
  });
