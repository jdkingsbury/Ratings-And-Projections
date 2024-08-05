import { PlayersDataTable } from "./data-table";
import { columns } from "./columns";
import { BACKEND_API_BASE_URL } from "@/components/utils/constants"

async function fetchPlayers() {
  const response = await fetch(`${BACKEND_API_BASE_URL}/nba/players`);
  if (!response.ok) {
    throw new Error("Failed to fetch players");
  }
  return response.json();
}

export default async function PlayersPage() {
  const players = await fetchPlayers();

  return (
    <div className="container py-10 mx-auto">
      <PlayersDataTable columns={columns} data={players} />
    </div>
  );
}
