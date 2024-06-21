import { LoaderFunctionArgs } from "@remix-run/node";
import { useLoaderData } from "@remix-run/react";
import Navbar from "~/components/navigation/navbar";

// NOTE: The loader function is used to fetch data for players info
export const loader = async ({ params }: LoaderFunctionArgs) => {
  const playerId = params.playerId;

  try {
    const resopnse = await fetch(
      `http://127.0.0.1:8000/nba/players/${playerId}`
    );
    if (!resopnse.ok) {
      throw new Error("failed to fetch player data");
    }

    const playerInfo = await resopnse.json();
    return playerInfo;
  } catch (error) {
    console.error("Failed to retrieve player data", error);
    throw error;
  }
};

// NOTE: The Player component is used to render player info
export default function Player() {
  const playerInfo = useLoaderData<typeof loader>();

  return (
    <div>
      <Navbar />
      <div>
        {playerInfo.map((player) => (
          <div key={player.PERSON_ID}>
            <img
              src={`https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/${player.PERSON_ID}.png`}
              alt={player.DISPLAY_FIRST_LAST}
            />
            <h1>{player.DISPLAY_FIRST_LAST}</h1>
          </div>
        ))}
      </div>
    </div>
  );
}
