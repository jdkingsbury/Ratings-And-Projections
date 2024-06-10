import { Link, Outlet } from "@remix-run/react";

export default function Players() {
  const players = [{ playerId: 2544, seasonId: "22023" }];

  return (
    <div>
      <h1>Players Page</h1>
      <ul>
        {players.map((player, index) => (
          <li key={index}>
            <Link to={`/players/${player.playerId}/${player.seasonId}`}>
              View Player Stats
            </Link>
          </li>
        ))}
      </ul>
      {/* NOTE: If you want to render the nested route, you need to use the Outlet */}
      <Outlet />
    </div>
  );
}
