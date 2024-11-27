import {axiosInstance} from "../axios-instance";

export async function apiFunc()  {
  const response = await axiosInstance.get();
  return response.data.data;
}
