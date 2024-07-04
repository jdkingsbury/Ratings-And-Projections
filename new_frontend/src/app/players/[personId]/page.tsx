import { Suspense } from "react";
import { PlayerBio } from "./player-info";
import { PlayerCareerStats } from "./player-career-stats";
import Loading from "@/app/loading";

async function PlayerInfo(personId) {
  const response = await fetch(
    `http://127.0.0.1:8000/nba/players/${personId}/player-info`,
  );
  return response.json();
}

async function CareerStats(personId) {
  const response = await fetch(
    `http://127.0.0.1:8000/nba/players/${personId}/career-stats`,
  );
  return response.json();
}

export default async function PlayerProfile({
  params,
}: {
  params: { personId: string };
}) {
  const [playerInfo, careerStats] = await Promise.all([
    PlayerInfo(params.personId),
    CareerStats(params.personId),
  ]);

  return (
    <div>
      <Suspense fallback={<Loading />}>
        <PlayerBio data={playerInfo} />
      </Suspense>
      <Suspense fallback={<Loading />}>
        <PlayerCareerStats data={careerStats} />
      </Suspense>
    </div>
  );
}
