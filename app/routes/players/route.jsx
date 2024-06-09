import { useLoaderData } from "@remix-run/react";
import { json } from "@remix-run/node";
import retrievePlayerGameLog from "../../db/retrieveQueries";

// NOTE: This is a loader function that will be called by Remix to fetch data from the database
export const loader = async () => {
  const playerId = 2544;
  const seasonId = "22023";

  try {
    const playerStats = await retrievePlayerGameLog(playerId, seasonId);
    return json({ playerStats });
  } catch (error) {
    console.error("Failed to retrieve player game log data", error);
    throw error;
  }
};

// NOTE: This is the React component that will render the data fetched from the database
export default function Players() {
  const { playerStats } = useLoaderData();

  if (!playerStats) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Lebron James</h1>
      <ul>
        {playerStats.map((stat, index) => (
          <li key={index}>
            {`Season: ${stat.season_id}, Points: ${stat.pts}, Assists: ${stat.ast}`}
          </li>
        ))}
      </ul>
    </div>
  );
}
