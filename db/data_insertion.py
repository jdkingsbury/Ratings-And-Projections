# Description: This file contains the functions to insert data into the database


# NOTE: Function to insert NBA players
def insert_nba_players(conn, players_data):
    cursor = conn.cursor()

    # NOTE: SQL statement to create the players table
    create_table_query = """
        CREATE TABLE IF NOT EXISTS players (
            person_id SERIAL PRIMARY KEY,
            display_last_comma_first VARCHAR(255),
            display_first_last VARCHAR(255),
            rosterstatus INT,
            from_year VARCHAR(4),
            to_year VARCHAR(4),
            playercode VARCHAR(255),
            player_slug VARCHAR(255),
            team_id INT,
            team_city VARCHAR(50),
            team_name VARCHAR(50),
            team_abbreviation VARCHAR(10),
            team_slug VARCHAR(50),
            team_code VARCHAR(50),
            games_played_flag CHAR(1),
            otherleague_experience_ch CHAR(2)
        );
        """
    cursor.execute(create_table_query)

    # NOTE: SQL statement to insert data into the players table
    insert_query = """
        INSERT INTO players (
            person_id, display_last_comma_first, display_first_last, rosterstatus, from_year, 
            to_year, playercode, player_slug, team_id, team_city, team_name, 
            team_abbreviation, team_slug, team_code, games_played_flag, otherleague_experience_ch
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (person_id) DO NOTHING;
        """

    try:
        for player in players_data:
            player_values = (
                player["PERSON_ID"],
                player["DISPLAY_LAST_COMMA_FIRST"],
                player["DISPLAY_FIRST_LAST"],
                player["ROSTERSTATUS"],
                player["FROM_YEAR"],
                player["TO_YEAR"],
                player["PLAYERCODE"],
                player["PLAYER_SLUG"],
                player["TEAM_ID"],
                player["TEAM_CITY"],
                player["TEAM_NAME"],
                player["TEAM_ABBREVIATION"],
                player["TEAM_SLUG"],
                player["TEAM_CODE"],
                player["GAMES_PLAYED_FLAG"],
                player["OTHERLEAGUE_EXPERIENCE_CH"],
            )
            cursor.execute(insert_query, player_values)
        conn.commit()
    except Exception as e:
        conn.rollback()  # Rollback the transaction on error
        print(f"An error occurred: {e}")


# NOTE: Function to insert player career stats
def insert_player_career_stats(conn, career_stats_data):
    cursor = conn.cursor()

    # NOTE: SQL statement to create the players table
    create_table_query = """
        CREATE TABLE IF NOT EXISTS player_career_stats (
            player_id INT,
            season_id VARCHAR(10),
            league_id VARCHAR(5),
            team_id INT,
            team_abbreviation VARCHAR(10),
            player_age DECIMAL,
            gp INT,
            gs INT,
            min DECIMAL,
            fgm INT,
            fga INT,
            fg_pct DECIMAL,
            fg3m INT,
            fg3a INT,
            fg3_pct DECIMAL,
            ftm INT,
            fta INT,
            ft_pct DECIMAL,
            oreb INT,
            dreb INT,
            reb INT,
            ast INT,
            stl INT,
            blk INT,
            tov INT,
            pf INT,
            pts INT,
            PRIMARY KEY (player_id, season_id),
            FOREIGN KEY (player_id) REFERENCES players(person_id)
        );
        """
    cursor.execute(create_table_query)

    # NOTE: SQL statement to insert data into the players table
    inser_query = """
        INSERT INTO player_career_stats (
            player_id, season_id, league_id, team_id, team_abbreviation, player_age, 
            gp, gs, min, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, 
            oreb, dreb, reb, ast, stl, blk, tov, pf, pts
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (player_id, season_id) DO UPDATE 
        SET 
            league_id = EXCLUDED.league_id, 
            team_id = EXCLUDED.team_id,
            team_abbreviation = EXCLUDED.team_abbreviation, 
            player_age = EXCLUDED.player_age, 
            gp = EXCLUDED.gp, 
            gs = EXCLUDED.gs, 
            min = EXCLUDED.min, 
            fgm = EXCLUDED.fgm, 
            fga = EXCLUDED.fga, 
            fg_pct = EXCLUDED.fg_pct, 
            fg3m = EXCLUDED.fg3m, 
            fg3a = EXCLUDED.fg3a, 
            fg3_pct = EXCLUDED.fg3_pct, 
            ftm = EXCLUDED.ftm, 
            fta = EXCLUDED.fta, 
            ft_pct = EXCLUDED.ft_pct, 
            oreb = EXCLUDED.oreb, 
            dreb = EXCLUDED.dreb, 
            reb = EXCLUDED.reb, 
            ast = EXCLUDED.ast, 
            stl = EXCLUDED.stl, 
            blk = EXCLUDED.blk, 
            tov = EXCLUDED.tov, 
            pf = EXCLUDED.pf, 
            pts = EXCLUDED.pts;
        """

    try:
        for stat in career_stats_data:
            player_career_stat_values = (
                stat["PLAYER_ID"],
                stat["SEASON_ID"],
                stat["LEAGUE_ID"],
                stat["TEAM_ID"],
                stat["TEAM_ABBREVIATION"],
                stat["PLAYER_AGE"],
                stat["GP"],
                stat["GS"],
                stat["MIN"],
                stat["FGM"],
                stat["FGA"],
                stat["FG_PCT"],
                stat["FG3M"],
                stat["FG3A"],
                stat["FG3_PCT"],
                stat["FTM"],
                stat["FTA"],
                stat["FT_PCT"],
                stat["OREB"],
                stat["DREB"],
                stat["REB"],
                stat["AST"],
                stat["STL"],
                stat["BLK"],
                stat["TOV"],
                stat["PF"],
                stat["PTS"],
            )
            cursor.execute(inser_query, player_career_stat_values)
        conn.commit()
    except Exception as e:
        conn.rollback()  # Rollback the transaction on error
        print(f"An error occurred: {e}")


# NOTE: Function to insert player game logs
def insert_player_game_log(conn, game_log_data):
    cursor = conn.cursor()

    # NOTE: SQL statement to create the players table
    create_table_query = """
        CREATE TABLE IF NOT EXISTS player_game_stats (
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
    """
    cursor.execute(create_table_query)

    # NOTE: SQL statement to insert data into the players table
    insert_query = """
        INSERT INTO player_game_stats (
            season_id, player_id, game_id, game_date, matchup, wl, min, 
            fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, 
            oreb, dreb, reb, ast, stl, blk, tov, pf, pts, plus_minus 
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
    """

    try:
        for data in game_log_data:
            data_values = (
                data["SEASON_ID"],
                data["Player_ID"],
                data["Game_ID"],
                data["GAME_DATE"],
                data["MATCHUP"],
                data["WL"],
                data["MIN"],
                data["FGM"],
                data["FGA"],
                data["FG_PCT"],
                data["FG3M"],
                data["FG3A"],
                data["FG3_PCT"],
                data["FTM"],
                data["FTA"],
                data["FT_PCT"],
                data["OREB"],
                data["DREB"],
                data["REB"],
                data["AST"],
                data["STL"],
                data["BLK"],
                data["TOV"],
                data["PF"],
                data["PTS"],
                data["PLUS_MINUS"],
            )
            cursor.execute(insert_query, data_values)

        conn.commit()
    except Exception as e:
        conn.rollback()  # Rollback the transaction on error
        print(f"An error occurred: {e}")


# NOTE: Function mapping for data insertion
function_mapping = {
    "get_player_career_stats": insert_player_career_stats,
    "get_all_players": insert_nba_players,
    "get_player_game_log": insert_player_game_log,
}
