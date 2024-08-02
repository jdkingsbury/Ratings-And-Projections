import { BACKEND_API_BASE_URL } from "@/components/utils/constants";
import { PlayerInfo } from "./player-info";
import { RecentGames } from "./recent-games";

async function fetchPlayerInfo(playerId: string) {
  const response = await fetch(
    `${BACKEND_API_BASE_URL}/nba/players/${playerId}`,
  );

  if (!response.ok) {
    throw new Error("Network response was not ok");
  }

  return response.json();
}

async function fetchPlayerRecentGames(playerId: string) {
  const response = await fetch(
    `${BACKEND_API_BASE_URL}/nba/players/${playerId}/recent_games`,
  );

  if (!response.ok) {
    throw new Error("Network resoponse was not ok");
  }

  return response.json();
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
      <div>
        <PlayerInfo data={playerInfo} />
        <RecentGames data={recentGames} />
      </div>
    );
  } catch (error) {
    console.error("Failed to fetch player info:", error);
    return <div>Error loading player info</div>;
  }
}
