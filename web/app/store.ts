import { configureStore } from "@reduxjs/toolkit";

import counterSlice from "./features/counter/counterSlice";
import pokemonSlice from "./features/pokemon/pokemonSlice";
import { pokemonApi } from "./features/pokemonApi/pokemonApi";
import { api } from "./services/apiService";

export const store = configureStore({
  reducer: {
    counter: counterSlice,
    pokemon: pokemonSlice,
    [pokemonApi.reducerPath]: pokemonApi.reducer,
    [api.reducerPath]: api.reducer,
  },

  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat([pokemonApi.middleware, api.middleware]),
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
