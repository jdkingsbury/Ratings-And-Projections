import { BACKEND_API_BASE_URL } from "@/components/utils/constants";
import { PlayerInfo } from "./player-info";
import { RecentGames } from "./recent-games";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import axios from "axios";
import { PlayerGameLog, Player } from "./types";

type FetchPlayerGameLog = {
  data: PlayerGameLog[] | null;
  error: string | null;
};

type FetchPlayerInfo = {
  data: Player | null;
  error: string | null;
};

async function fetchPlayerInfo(playerId: string): Promise<FetchPlayerInfo> {
  try {
    const response = await axios.get<Player>(
      `${BACKEND_API_BASE_URL}/nba/players/${playerId}`,
    );
    return { error: null, data: response.data };
  } catch (error: any) {
    console.error(`Failed to fetch player info: ${error.message}`);
    return { error: error.message, data: null };
  }
}

async function fetchPlayerRecentGames(
  playerId: string,
): Promise<FetchPlayerGameLog> {
  try {
    const response = await axios.get<PlayerGameLog[]>(
      `${BACKEND_API_BASE_URL}/nba/players/${playerId}/recent_games`,
    );
    return { error: null, data: response.data };
  } catch (error: any) {
    console.error(`Failed to fetch players recent games: ${error.message}`);
    return { error: error.message, data: null };
  }
}

// async function CareerStats(personId: string) {
//   const response = await fetch(
//     `${process.env.BACKEND_API_URL}/nba/players/${personId}/career-stats`,
//   );
//   return response.json();
// }

export default async function PlayerProfile({
  params,
}: {
  params: { playerId: string };
}) {
  try {
    const [playerInfo, recentGames] = await Promise.all([
      fetchPlayerInfo(params.playerId),
      fetchPlayerRecentGames(params.playerId),
    ]);

    return (
      <div className="p-6 min-h-screen">
        <div className="mb-6">
          <Card className="p-4 shadow-md rounded-lg w-full">
            <CardContent>
              {playerInfo.error ? (
                <p className="text-red-500">
                  Error when fetching player info: {playerInfo.error}
                </p>
              ) : !playerInfo.data ? (
                <p className="text-gray-500">Player not found.</p>
              ) : (
                <PlayerInfo data={playerInfo.data} />
              )}
            </CardContent>
          </Card>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card className="p-4 shadow-md rounded-lg col-span-1 lg:row-span-2">
            <CardHeader>
              <CardTitle>Recent Games</CardTitle>
            </CardHeader>
            <CardContent>
              {recentGames.error ? (
                <p className="text-red-500">
                  Error when fetching recent games: {recentGames.error}
                </p>
              ) : !recentGames.data ? (
                <p className="text-gray-500">Players recent games not found.</p>
              ) : (
                <RecentGames data={recentGames.data} />
              )}
            </CardContent>
          </Card>
        </div>
      </div>
    );
  } catch (error) {
    console.error("Failed to fetch player info:", error);
    return <div>Error loading player info</div>;
  }
}
