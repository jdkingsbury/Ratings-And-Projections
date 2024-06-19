import { Link, Outlet, useLoaderData } from "@remix-run/react";
import Nav from "../components/Nav";

export const loader = async () => {
  const response = await fetch("http://127.0.0.1:8000/nba/players");
  if (!response.ok) {
    throw new Error("failed to fetch players");
  }
  const players = await response.json();
  return players;
};

export default function Players() {
  const players = useLoaderData();

  return (
    <div>
      <Nav />
      <h1>Players Page</h1>
      <ul>
        {players.map((player) => (
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
