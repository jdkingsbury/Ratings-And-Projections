import { Link, Outlet, useLoaderData } from "@remix-run/react";
import Navbar from "~/components/navigation/navbar";

// NOTE: Define the shape of the data that will be fetched from the
interface Player {
  id: number;
  full_name: string;
  first_name: string;
  last_name: string;
  is_active: boolean;
  playerId: number;
}

export const loader = async () => {
  const response = await fetch("http://127.0.0.1:8000/nba/players");
  if (!response.ok) {
    throw new Error("failed to fetch players");
  }
  const players = await response.json();
  return players;
};

export default function Players() {
  const players = useLoaderData<typeof loader>();

  return (
    <div>
      <Navbar />
      <h1>Players Page</h1>
      <ul>
        {players.map((player: Player) => (
          <li key={player.id}>
            <Link to={`/players/${player.playerId}`}>
              {player.full_name}
            </Link>
          </li>
        ))}
      </ul>
      {/* NOTE: If you want to render the nested route, you need to use the Outlet */}
      <Outlet />
    </div>
  );
}
