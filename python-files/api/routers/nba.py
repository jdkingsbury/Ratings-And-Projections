from fastapi import APIRouter
from nba_api.stats.endpoints import (
    commonallplayers,
    cumestatsplayer,
    leaguedashplayerstats,
    playercareerstats,
    playergamelog,
)

router = APIRouter(prefix="/nba", tags=["nba"])

# NOTE: LeagueID: 00 = NBA, 10 = WNBA, 20 = G-League

# TODO:
# [] Work on implementing fast api into this project so that we can create api endpoints to use
# in the application but also allow others to access the data if we make it available to the public
# [] Clean up file and remove functions we do not need 
# [] Refactor functions so that they are cleaner


# NOTE: Get player stats for a specific season
def get_player_stats(season_year, output_format="json"):
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season_year, per_mode_detailed="PerGame"
    )
    player_stats = player_stats.get_data_frames()[0]
    relevant_columns = player_stats[
        [
            "PLAYER_NAME",
            "PTS",
            "AST",
            "REB",
            "STL",
            "BLK",
            "TOV",
            "FG_PCT",
            "FG3_PCT",
            "FT_PCT",
        ]
    ]

    if output_format == "csv":
        return relevant_columns.to_csv(index=False)
    elif output_format == "json":
        return relevant_columns.to_json(orient="records")
    else:
        raise ValueError("Unsupported format. Please choose 'json' or 'csv'.")


# This function will allow us to get the info of a specific player
def get_player_info(player_id, output_format="json"):
    player_info = CommonAllPlayers.CommonPlayerInfo(player_id=player_id)


# NOTE: Grabs all active players from NBA but not their info


@router.get("/players-all/{season_year}")
def get_all_players(season_year, output_format="json"):
    common_all_players = commonallplayers.CommonAllPlayers(
        is_only_current_season=1, league_id="00", season=season_year
    )

    df_common_all_players = common_all_players.get_data_frames()[0]

    # NOTE: Array of columns that aren't needed
    remove_cols = ["DISPLAY_LAST_COMMA_FIRST", "PLAYER_SLUG", "TEAM_SLUG"]

    for val in remove_cols:
        if val in df_common_all_players.columns:
            df_common_all_players = df_common_all_players.drop(columns=[val])

    # NOTE: Rename PERSON_ID to player_id
    df_common_all_players = df_common_all_players.rename(
        columns={"PERSON_ID": "PLAYER_ID"}
    )

    # NOTE: Add image url to each player
    df_common_all_players["IMAGE_URL"] = df_common_all_players["PLAYER_ID"].apply(
        lambda x: f"https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{x}.png"
    )

    if output_format == "csv":
        return df_common_all_players.to_csv(index=False)
    elif output_format == "json":
        return df_common_all_players.to_json(orient="records")
    else:
        raise ValueError("Unsupported format. Please choose 'json' or 'csv'.")


# NOTE: Gets player id from player name
def get_player_id(player_name, output_format="json"):
    common_all_players = commonallplayers.CommonAllPlayers(
        is_only_current_season=1, league_id="00"
    )
    df_common_all_players = common_all_players.get_data_frames()[0]
    player_id = df_common_all_players[
        df_common_all_players["DISPLAY_FIRST_LAST"] == player_name
    ]["PERSON_ID"]

    if output_format == "csv":
        return player_id.to_csv(index=False)
    elif output_format == "json":
        return player_id.to_json(orient="records")
    else:
        raise ValueError("Unsupported format. Please choose 'json' or 'csv'.")


# NOTE: Get player career stats
def get_player_career_stats(player_id, output_format="json"):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    player_career = career.get_data_frames()[0]

    if output_format == "csv":
        return player_career.to_csv(index=False)
    elif output_format == "json":
        return player_career.to_json(orient="records")
    else:
        raise ValueError("Unsupported format. Please choose 'json' or 'csv'.")


# NOTE: Get player game log
def get_player_game_log(player_id, season_year, output_format="json"):
    game_log = playergamelog.PlayerGameLog(
        player_id=player_id, season=season_year, season_type_all_star="Regular Season"
    )
    player_game_log = game_log.get_data_frames()[0]

    if "VIDEO_AVAILABLE" in player_game_log.columns:
        player_game_log = player_game_log.drop(columns=["VIDEO_AVAILABLE"])

    if output_format == "csv":
        return player_game_log.to_csv(index=False)
    elif output_format == "json":
        return player_game_log.to_json(orient="records", indent=4)
    else:
        raise ValueError("Unsupported format. Please choose 'json' or 'csv'.")


# TODO: Find out what game_ids are and how to get them
def get_player_cumulative_stats(player_id, game_ids, season_year, output_format="json"):
    stats = cumestatsplayer.CumeStatsPlayer(
        game_ids=game_ids,
        league_id="00",
        player_id=player_id,
        season=season_year,
        season_type_all_star="Regular Season",
    )
    player_stats = stats.get_data_frames()[0]

    if output_format == "csv":
        return player_stats.to_csv(index=False)
    elif output_format == "json":
        return player_stats.to_json(orient="records")
    else:
        raise ValueError("Unsupported format. Please choose 'json' or 'csv'.")
