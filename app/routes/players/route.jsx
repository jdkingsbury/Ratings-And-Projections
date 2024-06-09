import { useLoaderData } from "@remix-run/react";
import { json } from "@remix-run/node";
import retrievePlayerGameLog from "../../db/retrieveQueries";

// NOTE: This is a mock data loader that returns a static array of player stats.
// export const loader = async () => {
//   const playerStats = [
//     {
//       "SEASON_ID": "22023",
//       "Player_ID": 2544,
//       "Game_ID": "0022301195",
//       "GAME_DATE": "APR 14, 2024",
//       "MATCHUP": "LAL @ NOP",
//       "WL": "W",
//       "MIN": 38,
//       "FGM": 11,
//       "FGA": 20,
//       "FG_PCT": 0.55,
//       "FG3M": 0,
//       "FG3A": 2,
//       "FG3_PCT": 0.0,
//       "FTM": 6,
//       "FTA": 6,
//       "FT_PCT": 1.0,
//       "OREB": 2,
//       "DREB": 9,
//       "REB": 11,
//       "AST": 17,
//       "STL": 5,
//       "BLK": 1,
//       "TOV": 4,
//       "PF": 0,
//       "PTS": 28,
//       "PLUS_MINUS": 19
//     },
//   ];
//
//   return json({ playerStats });
// }

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

export default function Players() {
  const { playerStats } = useLoaderData();
  console.log("playerStats", playerStats);

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
