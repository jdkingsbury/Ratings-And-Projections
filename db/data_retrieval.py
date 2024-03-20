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
def get_season_average_field_goal_percentage(conn, player_id, season_id):
    cursor = conn.cursor()
    query = """
        SELECT AVG(fg_pct) AS season_average_field_goal_percentage
        FROM player_game_stats
        WHERE player_id = %s and season_id = %s 
    """
    cursor.execute(query, (player_id, season_id,))
    result = cursor.fetchone()
    cursor.close()

    return result[0] if result else None


# NOTE: Function to get total three pointers made and attempted
def get_season_average_three_point_percentage(conn, player_id, season_id):
    cursor = conn.cursor()
    query = """
        SELECT SUM(fg3_pct) AS season_average_three_point_percentage
        FROM player_game_stats
        WHERE player_id = %s and season_id = %s 
    """
    cursor.execute(query, (player_id, season_id))
    result = cursor.fetchone()
    cursor.close()
    return result


# NOTE: Function to get total free throws made and attempted
def get_season_average_free_throw_percentage(conn, player_id, season_id):
    cursor = conn.cursor()
    query = """
        SELECT SUM(ft_pct) AS season_average_free_throw_percentage
        FROM player_game_stats
        WHERE player_id = %s and season_id = %s 
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
    "get_season_average_field_goal_percentage": get_season_average_field_goal_percentage,
    "get_season_average_three_point_percentage": get_season_average_three_point_percentage,
    "get_season_average_free_throw_percentage": get_season_average_free_throw_percentage,
}
