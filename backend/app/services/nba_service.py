from nba_api.stats.static import players

def fetch_all_players():
    nba_players = players.get_players()
    return nba_players
