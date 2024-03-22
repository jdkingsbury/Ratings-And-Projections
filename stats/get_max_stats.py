from db.db_operations import connect_to_database

def get_max_stats(context, season=None):
    conn = connect_to_database()

    if not conn:
        raise Exception("Database connection failed")

    cursor = conn.cursor()

    if context == 'historical':
        query = """
        SELECT
            MAX(ppg) AS max_ppg,
            MAX(rpg) AS max_rpg,
            MAX(apg) AS max_apg,
            MAX(spg) AS max_spg,
            MAX(bpg) AS max_bpg,
            MIN(tov) AS min_tov,
            MAX(fg_percent) AS max_fg_percent,
            MAX(three_point_percent) AS max_three_point_percent,
            MAX(ft_percent) AS max_ft_percent
        FROM player_season_stats
        """
        cursor.execute(query)
    elif context == 'seasonal' and season is not None:
        query = """
        SELECT
            MAX(ppg) AS max_ppg,
            MAX(rpg) AS max_rpg,
            MAX(apg) AS max_apg,
            MAX(spg) AS max_spg,
            MAX(bpg) AS max_bpg,
            MIN(tov) AS min_tov,
            MAX(fg_percent) AS max_fg_percent,
            MAX(three_point_percent) AS max_three_point_percent,
            MAX(ft_percent) AS max_ft_percent
        FROM player_season_stats
        WHERE season_id = %s
        """
        cursor.execute(query, (season,))
    else:
        raise ValueError("Invalid context or season wasn't provided")

    result = cursor.fetchone()
    cursor.close()
    conn.close()

    return {
        "ppg": result[0],
        "rpg": result[1],
        "apg": result[2],
        "spg": result[3],
        "bpg": result[4],
        "tov": result[5],
        "fg_percent": result[6],
        "three_point_percent": result[7],
        "ft_percent": result[8],
    }
        
