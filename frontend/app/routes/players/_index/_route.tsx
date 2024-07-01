import { useLoaderData } from "@remix-run/react";
import Navbar from "~/components/navigation/navbar";
import PlayersDataTable from "./dataTable";
import { columns } from "./columns";

// TODO: Work on creating a better way to display the players. Maybe a table?

// NOTE: the loader function is used to fetch all players
export const loader = async () => {
  try {
    const response = await fetch("http://127.0.0.1:8000/nba/players");
    if (!response.ok) {
      throw new Error("failed to fetch players");
    }
    const players = await response.json();
    return players;
  } catch (error) {
    throw error;
  }
};

// NOTE: The ListPlayers component is used to render all players

export default function ListPlayers() {
  const players = useLoaderData<typeof loader>();

  return (
    <div>
      <Navbar />
      <PlayersDataTable columns={columns} data={players} />
    </div>
  );
}
