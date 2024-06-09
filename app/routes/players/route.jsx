import { useLoaderData } from "@remix-run/react";
import { json } from "@remix-run/node";
// import retrievePlayerGameLog from "~/db/reretrieveQueries";
import retrievePlayerGameLog from "../../db/retrieveQueries";

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
    const data = await retrievePlayerGameLog(playerId, seasonId);
    console.log(data);
    return json(data);
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export default function Players() {
  const { playerStats } = useLoaderData();

  return (
    <div>
      <h1>Lebron James</h1>
      <ul>
        {playerStats.map((stat, index) => (
          <li key={index}>
            {`Season: ${stat.SEASON_ID}, Points: ${stat.PTS}, Assists: ${stat.AST}`}
          </li>
        ))}
      </ul>
    </div>
  );
}
