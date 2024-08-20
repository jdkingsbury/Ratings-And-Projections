from datetime import datetime
from typing import Optional

from nba_api.stats.static import teams


# Get the current nba season
def get_current_season_year() -> str:
    current_date = datetime.now()
    year = current_date.year
    if current_date.month < 10:
        season_year = f"{year-1}-{str(year)[2:]}"
    else:
        season_year = f"{year}-{str(year+1)[2:]}"

    return season_year


def fetch_players_team(team_id: int) -> Optional[str]:
    team = teams.find_team_name_by_id(team_id)
    team_name = team["full_name"] if team else None

    return team_name
