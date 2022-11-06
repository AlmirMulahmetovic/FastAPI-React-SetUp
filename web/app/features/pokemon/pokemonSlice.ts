import axios from "axios";
import { createSlice, createAsyncThunk, PayloadAction } from "@reduxjs/toolkit";

import { RootState } from "@/app/store";

import { ErrorMessage, ThunkStatus } from "@/app/util";

export const fetchPokemons = createAsyncThunk(
  "pokemon/fetchPokemons",
  async () => {
    const response = await axios.get("https://pokeapi.co/api/v2/pokemon");
    return response.data.results;
  }
);

interface Pokemon {
  name: string;
  url: string;
}

interface PokemonState {
  data: Pokemon[];
  status: ThunkStatus;
  error: ErrorMessage;
}

const initialState: PokemonState = {
  data: [],
  status: ThunkStatus.IDLE,
  error: null,
};

export const pokemonSlice = createSlice({
  name: "pokemon",
  initialState,
  reducers: {},
  extraReducers(builder) {
    builder
      .addCase(fetchPokemons.pending, (state, _action) => {
        state.status = ThunkStatus.LOADING;
      })
      .addCase(
        fetchPokemons.fulfilled,
        (state, action: PayloadAction<Pokemon[]>) => {
          state.data = action.payload;
          state.status = ThunkStatus.SUCCEEDED;
        }
      )
      .addCase(fetchPokemons.rejected, (state, _action) => {
        state.status = ThunkStatus.FAILED;
        state.error = "Something went wrong";
      });
  },
});

export const selectPokemons = (state: RootState) => state.pokemon.data;

export default pokemonSlice.reducer;
