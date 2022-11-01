import React from "react";

import type { NextPage } from "next";
import { useGetPokemonsQuery } from "@/app/features/pokemonApi/pokemonApi";
import { useGetHelloWorldQuery } from "@/app/services/apiService";
import Link from "next/link";

import withBaseLayout from "@/components/layouts/base/withBaseLayout";

const Pokemon: NextPage = () => {
  const { data, error, isLoading } = useGetPokemonsQuery();
  console.log(data);

  return (
    <div style={{ margin: "20%" }}>
      <h3>Pokemons</h3>

      {data &&
        data.results &&
        data.results.map((pokemon: any) => (
          <div>
            <strong>{pokemon.name}</strong>
            <Link href={`pokemon/${pokemon.name}`}>
              <a>{pokemon.url}</a>
            </Link>
          </div>
        ))}
      {isLoading}
      {error}
    </div>
  );
};

export default withBaseLayout(Pokemon);
