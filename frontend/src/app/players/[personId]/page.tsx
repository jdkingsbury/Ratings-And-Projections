import { PlayerBio } from "./player-info";
import { PlayerCareerStats } from "./player-career-stats";
import { PlayerLast5Games } from "./last-5-games";

import { Suspense } from "react";
import Loading from "@/app/loading";

async function Last5Games(personId: string) {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/nba/players/${personId}/2023-24/5/player-game-log`,
  );
  return response.json();
}

async function PlayerInfo(personId: string) {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/nba/players/${personId}/player-info`,
  );
  return response.json();
}

async function CareerStats(personId: string) {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/nba/players/${personId}/career-stats`,
  );
  return response.json();
}

export default async function PlayerProfile({
  params,
}: {
  params: { personId: string };
}) {
  const [playerInfo, careerStats, last5Games] = await Promise.all([
    PlayerInfo(params.personId),
    CareerStats(params.personId),
    Last5Games(params.personId),
  ]);

  return (
    <div>
      <Suspense fallback={<Loading />}>
        <PlayerBio data={playerInfo} />
      </Suspense>
      <Suspense fallback={<Loading />}>
        <PlayerCareerStats data={careerStats} />
      </Suspense>
      <Suspense fallback={<Loading />}>
        <PlayerLast5Games data={last5Games} />
      </Suspense>
    </div>
  );
}
