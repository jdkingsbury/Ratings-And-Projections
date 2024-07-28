from datetime import datetime

# Get the current nba season
def get_current_season_year() -> str:
    current_date = datetime.now()
    year = current_date.year
    if current_date.month < 10:
        season_year = f"{year-1}-{str(year)[2:]}"
    else:
        season_year = f"{year}-{str(year+1)[2:]}"

    return season_year
