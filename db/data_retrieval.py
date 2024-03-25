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
    cursor.execute(query, (player_id, season_id))
    result = cursor.fetchone()
    cursor.close()
    return float(result[0]) if result else None


# NOTE: Function to get total three pointers made and attempted
def get_season_average_three_point_percentage(conn, player_id, season_id):
    cursor = conn.cursor()
    query = """
        SELECT AVG(fg3_pct) AS season_average_three_point_percentage
        FROM player_game_stats
        WHERE player_id = %s and season_id = %s 
    """
    cursor.execute(query, (player_id, season_id))
    result = cursor.fetchone()
    cursor.close()
    return float(result[0]) if result else None


# NOTE: Function to get total free throws made and attempted
def get_season_average_free_throw_percentage(conn, player_id, season_id):
    cursor = conn.cursor()
    query = """
        SELECT AVG(ft_pct) AS season_average_free_throw_percentage
        FROM player_game_stats
        WHERE player_id = %s and season_id = %s 
    """
    cursor.execute(query, (player_id, season_id))
    result = cursor.fetchone()
    cursor.close()
    return float(result[0]) if result else None

def get_max_player_stats(conn, season_id):
    cursor = conn.cursor()
    query = """
        SELECT 
        MAX(pts) AS max_points,
        MAX(reb) AS max_rebounds,
        MAX(ast) AS max_assists,
        MAX(stl) AS max_steals,
        MAX(blk) AS max_blocks,
        MAX(tov) AS max_turnovers,
        MAX(fg_pct) AS max_fg_percentage,
        MAX(fg3_pct) AS max_three_point_percentage,
        MAX(ft_pct) AS max_free_throw_percentage
        FROM player_stats
        WHERE season_id = %s
    """
    cursor.execute(query, (season_id,))
    result = cursor.fetchone()

    return {
        "max_points": result[0],
        "max_rebounds": result[1],
        "max_assists": result[2],
        "max_steals": result[3],
        "max_blocks": result[4],
        "max_turnovers": result[5],
        "max_fg_percentage": result[6],
        "max_three_point_percentage": result[7],
        "max_free_throw_percentage": result[8],
    }

def get_min_player_stats(conn, season_id):
    cursor = conn.cursor()
    query = """
        SELECT 
        MIN(pts) AS min_points,
        MIN(reb) AS min_rebounds,
        MIN(ast) AS min_assists,
        MIN(stl) AS min_steals,
        MIN(blk) AS min_blocks,
        MIN(tov) AS min_turnovers,
        MIN(fg_pct) AS min_fg_percentage,
        MIN(fg3_pct) AS min_three_point_percentage,
        MIN(ft_pct) AS min_free_throw_percentage
        FROM player_stats
        WHERE season_id = %s
    """
    cursor.execute(query, (season_id,))
    result = cursor.fetchone()

    return {
        "min_points": result[0],
        "min_rebounds": result[1],
        "min_assists": result[2],
        "min_steals": result[3],
        "min_blocks": result[4],
        "min_turnovers": result[5],
        "min_fg_percentage": result[6],
        "min_three_point_percentage": result[7],
        "min_free_throw_percentage": result[8],
    }

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
    "get_max_player_stats": get_max_player_stats,
    "get_min_player_stats": get_min_player_stats,
}
