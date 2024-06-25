import pandas as pd
from fastapi import APIRouter, Response
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
async def all_players():
    nba_players = players.get_players()
    active_players = [player for player in nba_players if player["is_active"] == True]
    return JSONResponse(content=active_players)


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
            "FG_PCT": "FG%",
            "FG3M": "3PM",
            "FG3A": "3PA",
            "FG3_PCT": "3P%",
            "FT_PCT": "FT%",
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


# NOTE: Get players game for the season
@router.get("/players/{person_id}/{season_year}/{games}/player-game-log")
async def get_player_game_log(
    person_id: int, season_year: str, games: int, output_format="json"
):
    # Gets the player game log for the season
    game_log = playergamelog.PlayerGameLog(player_id=person_id, season=season_year)
    player_game_log_df = game_log.get_data_frames()[0]

    # NOTE: Rename Columns
    player_game_log_df = player_game_log_df.rename(
        columns={
            "Player_ID": "PERSON_ID",
            "Game_ID": "GAME_ID",
            "FG_PCT": "FG%",
            "FG3M": "3PM",
            "FG3A": "3PA",
            "FG3_PCT": "3P%",
            "FT_PCT": "FT%",
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


# WARNING: This endpoint does not work
# TODO: Find out how to use video details or another endpoint to retrieve video for each game
# If we can't use it then we will need to find another way to get video for each game
# NOTE: This route will get the players games videos.
# Might not be able to use unless we have permission when the app is in live


@router.get("/players/{person_id}/{season_year}/{games}/video")
async def get_player_game_log_and_video(
    person_id: int, season_year: str, games: int, output_format="json"
):

    # Get player info to get team_id
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=person_id)
    player_info_df = player_info.get_data_frames()[0]

    team_id = player_info_df["TEAM_ID"].iloc[0]

    # Gets the player game log for the season
    game_log = playergamelog.PlayerGameLog(player_id=person_id, season=season_year)
    player_game_log_df = game_log.get_data_frames()[0]

    list_of_games = player_game_log_df.head(games)

    # Get video details for each game
    video_details_list = []

    # TODO: Check what video details returns since using get_data_frames is causing it to go out of range.
    # Possible that I may need to do something different.
    for _, game in list_of_games.iterrows():
        game_id = game["Game_ID"]
        video_details = videodetails.VideoDetails(
            player_id=person_id, team_id=team_id, game_id_nullable=game_id
        )
        video_details_df = video_details.get_data_frames()[0]
        video_details_list.append(video_details_df)

    # Combine all video details into one dataframe or return an empty list
    if video_details_list:
        all_video_details_df = pd.concat(video_details_list, ignore_index=True)
        video_details_json = all_video_details_df.to_dict(orient="records")
    else:
        video_details_json = []

    if output_format == "csv":
        player_game_log_csv = list_of_games.to_csv(index=False)
        return Response(content=player_game_log_csv, media_type="text/csv")
    elif output_format == "json":
        player_game_log_dict = list_of_games.to_dict(orient="records")
        response = {"games": player_game_log_dict, "videos": video_details_json}
        return JSONResponse(content=response)
    else:
        raise ValueError("Unsupported format. Please choose 'json' or 'csv'.")
