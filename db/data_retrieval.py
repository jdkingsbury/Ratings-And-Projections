# Description: This file contains the functions to retrieve data from the database

def get_total_points_and_games_played(conn, player_id, season_id):
    cursor = conn.cursor()

    query = """
        SELECT SUM(pts) AS total_points, COUNT(game_id) AS games_played
        FROM player_game_stats
        WHERE player_id = %s AND season_id = %s
        GROUP BY player_id
    """

    cursor.execute(query, (player_id, season_id))
    return cursor.fetchone()

retrieval_function_mapping = {
    "get_total_points_and_games_played": get_total_points_and_games_played,
}
