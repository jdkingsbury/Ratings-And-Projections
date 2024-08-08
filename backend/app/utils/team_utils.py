from typing import List

from nba_api.stats.static import teams


# function to fetch all team ids
def fetch_all_team_ids_nba() -> List[int]:
    all_teams = teams.get_teams()
    team_ids = [team["id"] for team in all_teams]
    return team_ids
