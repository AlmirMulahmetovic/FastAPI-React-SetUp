import type { NextPage } from "next";
import { useRouter } from "next/router";
import { useGetPokemonByNameQuery } from "@/app/features/pokemonApi/pokemonApi";
import withBaseLayout from "@/components/layouts/base/withBaseLayout";

const SinglePokemon: NextPage = () => {
  const router = useRouter();
  const { name } = router.query;

  const { data, error, isLoading } = useGetPokemonByNameQuery(
    (name as string) || "charmander"
  );

  return (
    <div style={{ margin: "20%" }}>
      <h3>Single pokemon</h3>
      {data && (
        <div>
          {data.name}: {data.id}: {data.weight}
        </div>
      )}
      {error}
      {isLoading}
    </div>
  );
};

export default withBaseLayout(SinglePokemon);
