import json
import nba_api.stats.endpoints as CommonAllPlayers

# LeagueID: 00 = NBA, 10 = WNBA, 20 = G-League

# Grab all active players from NBA
def get_all_players(season_year):
    common_all_players = CommonAllPlayers.CommonAllPlayers(
        is_only_current_season=1,
        league_id='00',
        season=season_year
    )
    df_common_all_players = common_all_players.get_data_frames()[0]
    return df_common_all_players.to_json(orient='records', lines=True)


print(get_all_players('2020-21'))

# # Anthony Davis
# career = playercareerstats.PlayerCareerStats(player_id="203076")
# career.get_data_frames()[0]
#
# print(career.get_data_frames()[0].head(1))

