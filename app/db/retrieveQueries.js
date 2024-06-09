import pool from "./db.js";

export default async function retrievePlayerGameLog(playerId, season_id) {
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
