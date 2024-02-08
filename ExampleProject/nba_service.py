import pandas as pd
import requests

from nba_api.stats import endpoints
 
# NBA API

# Fetch players and display league leaders
def get_league_leaders():
    data = endpoints.leagueleaders.LeagueLeaders() 
    df = data.league_leaders.get_data_frame()
    return df

print(get_league_leaders())

