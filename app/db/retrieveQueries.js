import { queryDatabase } from "../db/db.js";

// NOTE: Might change
async function retrievePlayerGameLog(playerId, season_id) {
  const query = `
    SELECT * FROM player_game_log
    WHERE player_id = $1 AND season_id = $2;
  `;

  return queryDatabase(query, [playerId, season_id]);
}

// async function getAllPlayers() {
// }

export const retrieveFunctionMap = {
  retrievePlayerGameLog,
};
