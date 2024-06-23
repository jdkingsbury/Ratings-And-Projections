from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from nba_api.stats.endpoints import (
    commonallplayers,
    commonplayerinfo,
    leaguedashplayerstats,
    playercareerstats,
    playergamelog,
)
from nba_api.stats.static import players

router = APIRouter(prefix="/nba", tags=["nba"])

# NOTE: LeagueID: 00 = NBA, 10 = WNBA, 20 = G-League
# person_id and player_id both represent player.
# The endpoints don't use the same name so I might need to find how I plan to keep it consistent

# NOTE: Possible endpoints
# Draft History
# Last 5 games
# Player News

# TODO:
# [x] Work on implementing fast api into this project so that we can create api endpoints to use
# in the application but also allow others to access the data if we make it available to the public
# [] Clean up file and remove functions we do not need
# [] Refactor functions so that they are cleaner

# PLAYERS


# NOTE: Will get the player_id from players name.
def get_player_id(player_name):
    player = players.find_players_by_full_name(player_name)[0]
    player_id = player["id"]
    return player_id


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


# NOTE: Static function that gets basic info for all players
# Might change how I retrieve all players
@router.get("/players")
def all_players():
    nba_players = players.get_players()
    active_players = [player for player in nba_players if player["is_active"] == True]
    return JSONResponse(content=active_players)


# This function will allow us to get the info of a specific player
@router.get("/players/{person_id}")
def get_player_info(person_id, output_format="json"):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=person_id)
    player_info_df = player_info.get_data_frames()[0]

    # Add image url to the dataframe
    player_info_df["IMAGE_URL"] = player_info_df["PERSON_ID"].apply(
        lambda x: f"https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{x}.png"
    )

    if output_format == "csv":
        player_info_csv = player_info_df.to_csv(index=False)
        return Response(content=player_info_csv, media_type="text/csv")
    elif output_format == "json":
        player_info_dict = player_info_df.to_dict(orient="records")
        return JSONResponse(content=player_info_dict)
    else:
        raise ValueError("Unsupported format. Please choose 'json' or 'csv'.")


# NOTE: Get player career stats
@router.get("/players/{person_id}/career-stats")
def get_player_career_stats(person_id, output_format="json"):
    player_career_stats = playercareerstats.PlayerCareerStats(player_id=person_id)
    player_career_stats_df = player_career_stats.get_data_frames()[0]

    # NOTE: Rename PLAYER_ID to PERSON_ID
    player_career_stats_df = player_career_stats_df.rename(
        columns={"PLAYER_ID": "PERSON_ID"}
    )

    if output_format == "csv":
        player_career_stats_csv = player_career_stats_df.to_csv(index=False)
        return Response(content=player_career_stats_csv, media_type="text/csv")
    elif output_format == "json":
        player_career_stats_dict = player_career_stats_df.to_dict(orient="records")
        return JSONResponse(content=player_career_stats_dict)
    else:
        raise ValueError("Unsupported format. Please choose 'json' or 'csv'.")


# NOTE: Get players game for the season
@router.get("/players/{person_id}/{season_year}/{games}")
async def get_player_game_log(person_id: int, season_year: str, games: str, output_format="json"):
    game_log = playergamelog.PlayerGameLog(player_id=person_id, season=season_year)
    player_game_log_df = game_log.get_data_frames()[0]
    
    if games!=0:
        player_game_log_df.head(5)

    if output_format == "csv":
        player_game_log_csv = player_game_log_df.to_csv(index=False)
        return Response(content=player_game_log_csv, media_type="text/csv")
    elif output_format == "json":
        player_game_log_dict = player_game_log_df.to_dict(orient="records")
        return JSONResponse(content=player_game_log_dict)
    else:
        raise ValueError("Unsupported format. Please choose 'json' or 'csv'.")
