import json
import nba_api.stats.endpoints as CommonAllPlayers
import nba_api.stats.endpoints as playercareerstats

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

# Get player id from player name
def get_player_id(player_name):
    common_all_players = CommonAllPlayers.CommonAllPlayers(
        is_only_current_season=1,
        league_id='00'
    )
    df_common_all_players = common_all_players.get_data_frames()[0]
    player_id = df_common_all_players[df_common_all_players['DISPLAY_FIRST_LAST'] == player_name]['PERSON_ID']
    return player_id.to_json(orient='records', lines=True)

# Get player career stats
def get_player_career_stats(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    return career.get_data_frames()[0].to_json(orient='records', lines=True)

print(get_player_career_stats(203076))

 # Anthony Davis
# career = playercareerstats.PlayerCareerStats(player_id="203076")
# career.get_data_frames()[0]
#
# print(career.get_data_frames()[0].head(1))

