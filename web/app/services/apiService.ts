import { PublicConfig } from "@/config/PublicConfig";
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const api = createApi({
  reducerPath: "mainApi",
  baseQuery: fetchBaseQuery({ baseUrl: PublicConfig.apiUrl(), credentials: "same-origin" }),
  endpoints: (builder) => ({
    getHelloWorld: builder.query<any, void>({
      query: () => "/",
    }),
  }),
});

// Export hooks for usage in functional components, which are
// auto-generated based on the defined endpoints
export const { useGetHelloWorldQuery } = api;
