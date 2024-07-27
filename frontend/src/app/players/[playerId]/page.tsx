import { BACKEND_API_BASE_URL } from "@/components/utils/constants";
import { PlayerBio } from "./player-info";

async function PlayerInfo(playerId: string) {
  const response = await fetch(
    `${BACKEND_API_BASE_URL}/nba/players/${playerId}`,
  );

  if (!response.ok) {
    throw new Error("Network response was not ok");
  }

  return response.json();
}

export default async function PlayerProfile({
  params,
}: {
  params: { playerId: string };
}) {
  try {
    const playerInfo = await PlayerInfo(params.playerId);

    return (
      <div>
        <PlayerBio data={playerInfo} />
      </div>
    );
  } catch (error) {
    console.error("Failed to fetch player info:", error);
    return <div>Error loading player info</div>;
  }
}
