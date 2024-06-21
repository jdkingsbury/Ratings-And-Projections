import { Link, Outlet, useLoaderData } from "@remix-run/react";
import Navbar from "~/components/navigation/navbar";

// NOTE: Used to define the shape of the data that will be fetched from the
interface Player {
  id: number;
  full_name: string;
  first_name: string;
  last_name: string;
  is_active: boolean;
  playerId: number;
}

// NOTE: the loader function is used to fetch all players
export const loader = async () => {
  const response = await fetch("http://127.0.0.1:8000/nba/players");
  if (!response.ok) {
    throw new Error("failed to fetch players");
  }
  const players = await response.json();
  return players;
};

// NOTE: The ListPlayers component is used to render all players
export default function ListPlayers() {
  const players = useLoaderData<typeof loader>();

  return (
    <div>
      <Navbar />
      <h1>Players Page</h1>
      <div id="players">
        {players.map((player: Player) => (
          <div key={player.id}>
            <Link to={`/players/${player.id}`}>{player.full_name}</Link>
            <Outlet />
          </div>
        ))}
      </div>

      {/* <ul> */}
      {/*   {players.map((player: Player) => ( */}
      {/*     <li key={player.id}> */}
      {/*       <Link to={`/players/${player.id}`}> */}
      {/*         {player.full_name} */}
      {/*       </Link> */}
      {/*     </li> */}
      {/*   ))} */}
      {/* </ul> */}
      {/* NOTE: If you want to render the nested route, you need to use the Outlet */}
      {/* <Outlet /> */}
    </div>
  );
}
