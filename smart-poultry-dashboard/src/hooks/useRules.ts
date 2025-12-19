import { useQuery, useMutation } from "@tanstack/react-query";
import * as api from "../api/rules";
import { queryClient } from "../helper/queryClient";

export const useRules = () =>
  useQuery({
    queryKey: ["rules"],
    queryFn: api.listRules,
  });

export const useCreateRule = () =>
  useMutation({
    mutationFn: api.createRule,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["rules"] });
    },
  });
