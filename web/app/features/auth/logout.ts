import axios from "@/util/axios";
import { AxiosResponse } from "axios";

export const logout = async (): Promise<AxiosResponse<any, any>> => {
  return await axios.post(
    "/logout",
  ).then(
    (response) => { 
      localStorage.removeItem("tokenExpiresAt")
      return response
    }
  ).catch(
    (response) => response
  )
}
