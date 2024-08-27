import { PlayersDataTable } from "./players-data-table";
import { columns } from "./columns";
import { BACKEND_API_BASE_URL } from "@/components/utils/constants";
import { Player } from "./types";
import axios from "axios";

type FetchPlayerData = {
  data: Player[] | null;
  error: string | null;
};

async function fetchPlayers(): Promise<FetchPlayerData> {
  try {
    const response = await axios.get<Player[]>(
      `${BACKEND_API_BASE_URL}/nba/players`,
    );
    return { error: null, data: response.data };
  } catch (error: any) {
    console.error(`Failed to fetch players: ${error.message}`);
    return { error: error.message, data: null };
  }
}

export default async function PlayersPage() {
  const { data: players, error } = await fetchPlayers();

  return (
    <div className="container py-10 mx-auto">
      {error ? (
        <p>Error fetching players: {error}</p>
      ) : !players ? (
        <p>Players not found.</p>
      ) : (
        <PlayersDataTable columns={columns} data={players} />
      )}
    </div>
  );
}
