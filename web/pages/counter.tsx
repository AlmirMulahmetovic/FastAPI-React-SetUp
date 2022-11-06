import { ChangeEvent, useState, useEffect } from "react";
import type { NextPage } from "next";

import { useAppSelector, useAppDispatch } from "@/app/hooks";
import {
  increment,
  decrement,
  incrementByAmount,
  selectCount,
} from "@/app/features/counter/counterSlice";

import {
  fetchPokemons,
  selectPokemons,
} from "@/app/features/pokemon/pokemonSlice";

const Counter: NextPage = () => {
  const count = useAppSelector(selectCount);
  const pokemons = useAppSelector(selectPokemons);

  const dispatch = useAppDispatch();

  const [amount, setAmount] = useState(0);

  useEffect(() => {
    dispatch(fetchPokemons());
  }, []);

  return (
    <div style={{ margin: "20%" }}>
      <div style={{ display: "flex" }}>
        <button type="button" onClick={() => dispatch(decrement())}>
          -
        </button>
        <button type="button" onClick={() => dispatch(increment())}>
          +
        </button>
      </div>
      <div>
        <input
          type="number"
          value={amount}
          onChange={(event: ChangeEvent<HTMLInputElement>) =>
            setAmount(Number(event.target.value))
          }
        />
        <button
          type="button"
          onClick={() => dispatch(incrementByAmount(amount))}
        >
          Increment by amount
        </button>
      </div>
      <div>Current count {count}</div>
      <hr />
      <h3>Pokemons</h3>
      <div>
        {pokemons.map((pokemon) => (
          <div style={{ display: "flex" }} key={pokemon.name}>
            <div>
              <strong>{pokemon.name}: </strong>{" "}
            </div>{" "}
            <a href={pokemon.url} style={{ color: "blue" }}>
              {pokemon.url}
            </a>{" "}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Counter;
