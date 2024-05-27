const pool = require("./db");

const retrievePlayerGameLog = async (playerId, season_id) => {
  const query = `
    SELECT * FROM player_game_logs
    WHERE player_id = $1 AND season_id = $2;
  `;

  try {
    const res = await pool.query(query, [playerId, season_id]);
    return res.rows;
  } catch (err) {
    console.error(err.message);
    throw err;
  }
};

module.exports = { retrievePlayerGameLog };
