import { LoaderFunctionArgs } from "@remix-run/node";
import { Await, defer, useLoaderData } from "@remix-run/react";
import { Suspense } from "react";
import Navbar from "~/components/navigation/navbar";
import BasicInfo from "./basicInfo";
import PlayerCareerStats from "./careerStats";

// TODO: Check to see when we should use Await and defer

// NOTE: The loader function is used to fetch data for players info
export const loader = async ({ params }: LoaderFunctionArgs) => {
  const personId = params.personId;

  try {
    const [playerInfoResponse, careerStatsResponse] = await Promise.all([
      fetch(`http://127.0.0.1:8000/nba/players/${personId}`),
      fetch(`http://127.0.0.1:8000/nba/players/${personId}/career-stats`),
    ]);

    if (!playerInfoResponse.ok || !careerStatsResponse.ok) {
      throw new Error("Failed to retrieve player data");
    }

    const [playerInfo, careerStats] = await Promise.all([
      playerInfoResponse.json(),
      careerStatsResponse.json(),
    ]);

    return defer({ playerInfo, careerStats });
  } catch (error) {
    console.error("Failed to retrieve player data", error);
    throw error;
  }
};

// NOTE: The Player component is used to render player info
export default function PlayerProfile() {
  const { playerInfo, careerStats } = useLoaderData<typeof loader>();

  return (
    <>
      <Navbar />
      <Suspense fallback={<div>Loading...</div>}>
        <Await resolve={playerInfo}>
          {(playerInfo) => <BasicInfo player={playerInfo} />}
        </Await>
        <Await resolve={careerStats}>
          {(careerStats) => <PlayerCareerStats player={careerStats} />}
        </Await>
      </Suspense>
    </>
  );
}
