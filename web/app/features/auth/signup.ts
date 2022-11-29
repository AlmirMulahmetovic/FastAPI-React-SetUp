import axios from "@/util/axios";
import { AxiosResponse } from "axios";

export interface SignUpCredentials {
    email: FormDataEntryValue | null,
    password: FormDataEntryValue | null
    firstName: FormDataEntryValue | null
    lastName: FormDataEntryValue | null
}

export const signUp = async (signUpCredentials: SignUpCredentials): Promise<AxiosResponse> => {
  return await axios.post(
    "/sign-up",
    signUpCredentials
  ).then(
    (response) => {
      localStorage.setItem("tokenExpiresAt", response.data.tokenExpiresAt)
      return response
    }
  ).catch(
    (reason) => reason.response
  )
}
