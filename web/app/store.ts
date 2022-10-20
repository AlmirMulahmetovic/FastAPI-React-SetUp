import { configureStore } from "@reduxjs/toolkit";

import counterSlice from "./features/counter/counterSlice";
import pokemonSlice from "./features/pokemon/pokemonSlice";

export const store = configureStore({
  reducer: { counter: counterSlice, pokemon: pokemonSlice },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
