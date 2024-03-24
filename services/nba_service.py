import nba_api.stats.endpoints as CommonAllPlayers
import nba_api.stats.endpoints as playercareerstats
import nba_api.stats.endpoints as cumestatsplayer
import nba_api.stats.endpoints as playergamelog
import nba_api.stats.endpoints as leaguedashplayerstats


# NOTE: LeagueID: 00 = NBA, 10 = WNBA, 20 = G-League

# NOTE: Get player stats for a specific season
def get_player_stats(season_year):
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season_year, 
        per_mode_detailed='PerGame'
    )
    player_stats = player_stats.get_data_frames()[0]
    relevant_columns = player_stats[['PLAYER_NAME', 'PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FG_PCT', 'FG3_PCT', 'FT_PCT']]
    return relevant_columns.to_json(orient="records")

# NOTE: Grabs all active players from NBA
def get_all_players(season_year):
    common_all_players = CommonAllPlayers.CommonAllPlayers(
        is_only_current_season=1, 
        league_id="00", 
        season=season_year
    )
    df_common_all_players = common_all_players.get_data_frames()[0]
    return df_common_all_players.to_json(orient="records")


# NOTE: Gets player id from player name
def get_player_id(player_name):
    common_all_players = CommonAllPlayers.CommonAllPlayers(
        is_only_current_season=1, 
        league_id="00"
    )
    df_common_all_players = common_all_players.get_data_frames()[0]
    player_id = df_common_all_players[
        df_common_all_players["DISPLAY_FIRST_LAST"] == player_name
    ]["PERSON_ID"]
    return player_id.to_json(orient="records")


# NOTE: Get player career stats
def get_player_career_stats(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    player_career = career.get_data_frames()[0]
    return player_career.to_json(orient="records")


# NOTE: Get player game log
def get_player_game_log(player_id, season_year):
    game_log = playergamelog.PlayerGameLog(
        player_id=player_id, 
        season=season_year, 
        season_type_all_star="Regular Season"
    )
    player_game_log = game_log.get_data_frames()[0]

    if "VIDEO_AVAILABLE" in player_game_log.columns:
        player_game_log = player_game_log.drop(columns=["VIDEO_AVAILABLE"])

    return player_game_log.to_json(orient="records")


# TODO: Find out what game_ids are and how to get them
def get_player_cumulative_stats(player_id, game_ids, season_year):
    stats = cumestatsplayer.CumeStatsPlayer(
        game_ids=game_ids,
        league_id="00",
        player_id=player_id,
        season=season_year,
        season_type_all_star="Regular Season",
    )
    player_stats = stats.get_data_frames()[0]
    return player_stats.to_json(orient="records")
