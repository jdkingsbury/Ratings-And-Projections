import Navbar from "@/components/navbar-menu";
import { PlayersDataTable } from "./data-table";
import { columns } from "./columns";

const fetchPlayers = async () => {
  const response = await fetch("http://127.0.0.1:8000/nba/players");
  if (!response.ok) {
    throw new Error("Failed to fetch players");
  }
  return response.json();
};

export default async function PlayersPage() {
  const players = await fetchPlayers();

  return (
    <div className="container py-10 mx-auto">
      <PlayersDataTable columns={columns} data={players} />
    </div>
  );
}
