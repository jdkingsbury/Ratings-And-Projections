import { PlayerBio } from "./player-info";
import { PlayerCareerStats } from "./player-career-stats";
import { PlayerLast5Games } from "./last-5-games";

import { Suspense } from "react";
import Loading from "@/app/loading";

// async function Last5Games(personId: string) {
//   const response = await fetch(
//     `${process.env.BACKEND_API_URL}/nba/players/${personId}/2023-24/5/player-game-log`,
//   );
//   return response.json();
// }

async function PlayerInfo(playerId: string) {
  const response = await fetch(
    `${process.env.BACKEND_API_URL}/nba/players/${playerId}`,
  );
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
  // const [playerInfo, careerStats, last5Games] = await Promise.all([
  //   PlayerInfo(params.playerId),
  //   CareerStats(params.playerId),
  //   Last5Games(params.playerId),
  // ]);
  //
  const playerInfo = await PlayerInfo(params.playerId)

  return (
    <div>
      <Suspense fallback={<Loading />}>
        <PlayerBio data={playerInfo} />
      </Suspense>
      {/* <Suspense fallback={<Loading />}> */}
      {/*   <PlayerCareerStats data={careerStats} /> */}
      {/* </Suspense> */}
      {/* <Suspense fallback={<Loading />}> */}
      {/*   <PlayerLast5Games data={last5Games} /> */}
      {/* </Suspense> */}
    </div>
  );
}
