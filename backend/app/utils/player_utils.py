from typing import List
from nba_api.stats.static import players

def fetch_all_player_ids_nba() -> List[int]:
    all_players = players.get_players()
    active_players = [player for player in all_players if player["is_active"]]
    player_ids = [player["id"] for player in active_players]
    return player_ids
