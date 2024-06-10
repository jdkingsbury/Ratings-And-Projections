import pool from "./db.js";

async function retrievePlayerGameLog(playerId, season_id) {
  if (!pool) {
    console.error("Database pool is not connected");
    throw new Error("Database pool is not connected");
  }
  const query = `
    SELECT * FROM player_game_log
    WHERE player_id = $1 AND season_id = $2;
  `;

  try {
    const res = await pool.query(query, [playerId, season_id]);
    return res.rows;
  } catch (err) {
    console.error(err.message);
    throw err;
  }
}

export const retrieveFunctionMap = {
  retrievePlayerGameLog,
};
