import axios from "@/util/axios";
import { AxiosResponse } from "axios";

export interface LoginCredentials {
  email: FormDataEntryValue | null,
  password: FormDataEntryValue | null
}

export const login = async (loginCredentials: LoginCredentials): Promise<AxiosResponse> => {
  return await axios.post(
    "/login",
    loginCredentials
  ).then(
    (response) => {
      localStorage.setItem("tokenExpiresAt", response.data.tokenExpiresAt)
      return response
    }
  ).catch(
    (reason) => reason.response
  )
}
