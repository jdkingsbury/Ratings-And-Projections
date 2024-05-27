const pool = require("./db");

const insertPlayerGameLog = async (data) => {
  // NOTE: SQL query to player_game_stats table
  const createTableQuery = `
    CREATE TABLE IF NOT EXISTS player_game_logs (
    season_id VARCHAR(10),
    player_id INT,
    game_id VARCHAR(15),
    game_date DATE,
    matchup VARCHAR(15),
    wl CHAR(1),
    min INT,
    fgm INT,
    fga INT,
    fg_pct FLOAT,
    fg3m INT,
    fg3a INT,
    fg3_pct FLOAT,
    ftm INT,
    fta INT,
    ft_pct FLOAT,
    oreb INT,
    dreb INT,
    reb INT,
    ast INT,
    stl INT,
    blk INT,
    tov INT,
    pf INT,
    pts INT,
    plus_minus INT
    );
  `;

  const insertQuery = `
    INSERT INTO player_game_logs (
      season_id, player_id, game_id, game_date, matchup, wl, min, 
      fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, 
      oreb, dreb, reb, ast, stl, blk, tov, pf, pts, plus_minus 
    ) VALUES (
      $1, $2, $3, $4, $5, $6, $7, 
      $8, $9, $10, $11, $12, $13, $14, $15, $16, 
      $17, $18, $19, $20, $21, $22, $23, $24, $25, $26
    )
    RETURNING *;
  `;

  try {
    // NOTE: Create table if it doesn't exists
    await pool.query(createTableQuery);
    console.log("Table created or already exists");

    // NOTE: Insert data into the table
    for (let item of data) {
      const values = [
        item.SEASON_ID,
        item.Player_ID,
        item.GAME_ID,
        item.GAME_DATE,
        item.MATCHUP,
        item.WL,
        item.MIN,
        item.FGM,
        item.FGA,
        item.FG_PCT,
        item.FG3M,
        item.FG3A,
        item.FG3_PCT,
        item.FTM,
        item.FTA,
        item.FT_PCT,
        item.OREB,
        item.DREB,
        item.REB,
        item.AST,
        item.STL,
        item.BLK,
        item.TOV,
        item.PF,
        item.PTS,
        item.PLUS_MINUS,
      ];
      const res = await pool.query(insertQuery, values);
      console.log("Inserted player game log:", res.rows[0]);
    }
  } catch (err) {
    console.error("Error inserting player game log:", err);
    throw err;
  }
};

module.exports = { insertPlayerGameLog };
