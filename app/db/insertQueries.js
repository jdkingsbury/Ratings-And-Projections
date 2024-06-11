import pool from "./db.js";

// NOTE: THe createTableQuery's will probably be removed eventually and are being used for testing purposes

async function insertPlayerGameLog(data) {
  // NOTE: SQL query to player_game_stats table
  const createTableQuery = `
    CREATE TABLE IF NOT EXISTS player_game_log (
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
    INSERT INTO player_game_log (
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
}

async function getAllPlayers(data) {
  const createTableQuery = `
    CREATE TABLE IF NOT EXISTS players (
      player_id INT PRIMARY KEY,
      display_last_comma_first VARCHAR(255),
      display_first_last VARCHAR(255),
      rosterstatus INT,
      from_year varchar(4),
      to_year varchar(4),
      playercode varchar(255),
      player_slug varchar(255),
      team_id INT,
      team_city varchar(50),
      team_name varchar(50),
      team_abbreviation varchar(10),
      team_slug varchar(50),
      team_code varchar(50),
      games_played_flag varchar(1),
      other_league_experience_ch varchar(2),
      image_url blob
  `;

  const insertQuery = `
    INSERT INTO players (
      player_id, display_last_comma_first, display_first_last, rosterstatus, from_year, to_year, playercode, 
      player_slug, team_id, team_city, team_name, team_abbreviation, team_slug, team_code, 
      games_played_flag, otherleague_experience_ch, image_url
    ) VALUES (
      $1, $2, $3, $4, $5, $6, $7, 
      $8, $9, $10, $11, $12, $13, $14, 
      $15, $16
    )
    RETURNING *;
  `;

  try {
    // NOTE: Create Table if it does not exist 
    await pool.query(createTableQuery);
    console.log("Table created or already exitst");

    // NOTE: Insert data into table
    for (let item of data) {
      const values = [
        item.PLAYER_ID,
        item.DISPLAY_LAST_COMMA_FIRST,
        item.DISPLAY_FIRST_LAST,
        item.ROSTERSTATUS,
        item.FROM_YEAR,
        item.TO_YEAR,
        item.PLAYERCODE,
        item.PLAYER_SLUG,
        item.TEAM_ID,
        item.TEAM_CITY,
        item.TEAM_NAME,
        item.TEAM_ABBREVIATION,
        item.TEAM_SLUG,
        item.TEAM_CODE,
        item.GAMES_PLAYED_FLAG,
        item.OTHERLEAGUE_EXPERIENCE_CH,
        item.IMAGE_URL,
      ];
      const res = await pool.query(insertQuery, values);
      console.log("Inserted player data:", res.rows[0]);
    }
  } catch (err) {
    console.log("Error inserting player data:", err);
    throw err;
  }
}

export const insertFunctionMap = {
  insertPlayerGameLog,
  getAllPlayers,
};
