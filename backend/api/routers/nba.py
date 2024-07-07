import pandas as pd
from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse
from nba_api.stats.endpoints import (
    commonplayerinfo,
    playercareerstats,
    playergamelog,
    videodetails,
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


# NBA PLAYERS ENDPOINTS


# NOTE: Will get the player_id from players name.
def get_player_id(player_name: str):
    player = players.find_players_by_full_name(player_name)[0]
    player_id = player["id"]
    return player_id


# NOTE: Static function that gets basic info for all players
# Might change how I retrieve all players
@router.get("/players")
async def get_all_players(active=True):
    nba_players = players.get_players()
    if active:
        active_players = [
            player for player in nba_players if player["is_active"] == True
        ]
        return JSONResponse(content=active_players)
    else:
        return JSONResponse(content=nba_players)


# NOTE: This function will allow us to get the info of a specific player
@router.get("/players/{person_id}/player-info")
async def get_player_info(person_id: int, output_format="json"):
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
async def get_player_career_stats(person_id: int, output_format="json"):
    player_career_stats = playercareerstats.PlayerCareerStats(player_id=person_id)
    player_career_stats_df = player_career_stats.get_data_frames()[0]

    # NOTE: Rename Columns
    player_career_stats_df = player_career_stats_df.rename(
        columns={
            "PLAYER_ID": "PERSON_ID",
        }
    )

    if output_format == "csv":
        player_career_stats_csv = player_career_stats_df.to_csv(index=False)
        return Response(content=player_career_stats_csv, media_type="text/csv")
    elif output_format == "json":
        player_career_stats_dict = player_career_stats_df.to_dict(orient="records")
        return JSONResponse(content=player_career_stats_dict)
    else:
        raise ValueError("Unsupported format. Please choose 'json' or 'csv'.")


@router.get("/players/{person_id}/{season_year}/{games}/player-game-log")
async def get_player_game_log(
    person_id: int, season_year: str, games: int, output_format="json"
):
    """
    Fetches the players game log for a specific season for the number of games requested

    Parameters:
    - person_id (int): The ID of the player
    - season_year (str): The season year (e.g., 2023-24)
    - games (int): Number of games
    - output_format (str): format of the output, either json or csv. Defaults to json
    """
    # Gets the player game log for the season
    game_log = playergamelog.PlayerGameLog(player_id=person_id, season=season_year)
    player_game_log_df = game_log.get_data_frames()[0]

    # NOTE: Rename Columns
    player_game_log_df = player_game_log_df.rename(
        columns={
            "Player_ID": "PERSON_ID",
            "Game_ID": "GAME_ID",
        }
    )

    list_of_games = player_game_log_df.head(games)

    if output_format == "csv":
        player_game_log_csv = list_of_games.to_csv(index=False)
        return Response(content=player_game_log_csv, media_type="text/csv")
    elif output_format == "json":
        player_game_log_dict = list_of_games.to_dict(orient="records")
        return JSONResponse(content=player_game_log_dict)
    else:
        raise ValueError("Unsupported format. Please choose 'json' or 'csv'.")
