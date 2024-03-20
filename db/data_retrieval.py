# Description: This file contains the functions to retrieve data from the database


# NOTE: Function to get total points and games played
def get_total_points_and_games_played(conn, player_id, season_id):
    cursor = conn.cursor()

    query = """
        SELECT SUM(pts) AS total_points, COUNT(game_id) AS games_played
        FROM player_game_stats
        WHERE player_id = %s AND season_id = %s
        GROUP BY player_id
    """

    cursor.execute(query, (player_id, season_id))
    result = cursor.fetchone()
    cursor.close()

    return result


# NOTE: Function to get total rebounds and games played
def get_total_rebounds_and_games_played(conn, player_id, season_id):
    cursor = conn.cursor()
    query = """
        SELECT SUM(reb) AS total_rebounds, COUNT(game_id) AS games_played
        FROM player_game_stats
        WHERE player_id = %s AND season_id = %s
        GROUP BY player_id
    """
    cursor.execute(query, (player_id, season_id))
    result = cursor.fetchone()
    cursor.close()
    return result


# NOTE: Function to get total assists and games played
def get_total_assists_and_games_played(conn, player_id, season_id):
    cursor = conn.cursor()
    query = """
        SELECT SUM(ast) AS total_assists, COUNT(game_id) AS games_played
        FROM player_game_stats
        WHERE player_id = %s AND season_id = %s
        GROUP BY player_id
    """
    cursor.execute(query, (player_id, season_id))
    result = cursor.fetchone()
    cursor.close()
    return result


# NOTE: Function to get total steals and games played
def get_total_steals_and_games_played(conn, player_id, season_id):
    cursor = conn.cursor()
    query = """
        SELECT SUM(stl) AS total_steals, COUNT(game_id) AS games_played
        FROM player_game_stats
        WHERE player_id = %s AND season_id = %s
        GROUP BY player_id
    """
    cursor.execute(query, (player_id, season_id))
    result = cursor.fetchone()
    cursor.close()
    return result


# NOTE: Function to get total blocks and games played
def get_total_blocks_and_games_played(conn, player_id, season_id):
    cursor = conn.cursor()
    query = """
        SELECT SUM(blk) AS total_blocks, COUNT(game_id) AS games_played
        FROM player_game_stats
        WHERE player_id = %s AND season_id = %s
        GROUP BY player_id
    """
    cursor.execute(query, (player_id, season_id))
    result = cursor.fetchone()
    cursor.close()
    return result


# NOTE: Function to get total turnovers and games played
def get_total_turnovers_and_games_played(conn, player_id, season_id):
    cursor = conn.cursor()
    query = """
        SELECT SUM(tov) AS total_turnovers, COUNT(game_id) AS games_played
        FROM player_game_stats
        WHERE player_id = %s AND season_id = %s
        GROUP BY player_id
    """
    cursor.execute(query, (player_id, season_id))
    result = cursor.fetchone()
    cursor.close()
    return result


# NOTE: Function to get total field goals made and attempted
def get_total_field_goals_made_and_attempted(conn, player_id, season_id):
    cursor = conn.cursor()
    query = """
        SELECT SUM(fgm) AS total_field_goals_made, SUM(fga) AS total_field_goals_attempted
        FROM player_game_stats
        WHERE player_id = %s AND season_id = %s
        GROUP BY player_id
    """
    cursor.execute(query, (player_id, season_id))
    result = cursor.fetchone()
    cursor.close()
    return result


# NOTE: Function to get total three pointers made and attempted
def get_total_three_pointers_made_and_attempted(conn, player_id, season_id):
    cursor = conn.cursor()
    query = """
        SELECT SUM(three_m) AS total_three_pointers_made, SUM(three_a) AS total_three_pointers_attempted
        FROM player_game_stats
        WHERE player_id = %s AND season_id = %s
        GROUP BY player_id
    """
    cursor.execute(query, (player_id, season_id))
    result = cursor.fetchone()
    cursor.close()
    return result


# NOTE: Function to get total free throws made and attempted
def get_total_free_throws_made_and_attempted(conn, player_id, season_id):
    cursor = conn.cursor()
    query = """
        SELECT SUM(ftm) AS total_free_throws_made, SUM(fta) AS total_free_throws_attempted
        FROM player_game_stats
        WHERE player_id = %s AND season_id = %s
        GROUP BY player_id
    """
    cursor.execute(query, (player_id, season_id))
    result = cursor.fetchone()
    cursor.close()
    return result


retrieval_function_mapping = {
    "get_total_points_and_games_played": get_total_points_and_games_played,
    "get_total_rebounds_and_games_played": get_total_rebounds_and_games_played,
    "get_total_assists_and_games_played": get_total_assists_and_games_played,
    "get_total_steals_and_games_played": get_total_steals_and_games_played,
    "get_total_blocks_and_games_played": get_total_blocks_and_games_played,
    "get_total_turnovers_and_games_played": get_total_turnovers_and_games_played,
    "get_total_field_goals_made_and_attempted": get_total_field_goals_made_and_attempted,
    "get_total_three_pointers_made_and_attempted": get_total_three_pointers_made_and_attempted,
    "get_total_free_throws_made_and_attempted": get_total_free_throws_made_and_attempted,
}
