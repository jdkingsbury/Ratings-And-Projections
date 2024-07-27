import sys
import os

# Placed in to fix path issue. Will not need in docker but need if running locally
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, project_root)

import asyncio
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from app.utils.fetch_utils import fetch_data_async
from tqdm.asyncio import tqdm


# Needs to get season year as a parameter like 2023-24
def fetch_player_game_logs(player_id: int, season_year: str):
    player_game_log = playergamelog.PlayerGameLog(
        player_id=player_id, season=season_year
    )
    player_game_log_df = player_game_log.get_data_frames()[0]

    player_game_log_df = player_game_log_df.rename(
        columns={
            "SEASON_ID": "season_id",
            "Player_ID": "player_id",
            "Game_ID": "game_id",
            "GAME_DATE": "game_date",
            "MATCHUP": "matchup",
            "WL": "wl",
            "MIN": "min",
            "FGM": "fgm",
            "FGA": "fga",
            "FG_PCT": "fg_pct",
            "FG3M": "fg3m",
            "FG3_PCT": "fg3_pct",
            "FTM": "ftm",
            "FTA": "fta",
            "FT_PCT": "ft_pct",
            "OREB": "oreb",
            "DREB": "dreb",
            "REB": "reb",
            "AST": "ast",
            "STL": "stl",
            "BLK": "blk",
            "TOV": "tov",
            "PF": "pf",
            "PTS": "pts",
            "PLUS_MINUS": "plus_minus",
            "VIDEO_AVAILABLE": "video_available",
        }
    )

    return player_game_log_df


# NOTE: Will probably be made into a utility function
# Function to get all active players IDs
def get_all_player_ids():
    all_players = players.get_players()
    active_players = [player for player in all_players if player["is_active"]]
    player_ids = [player["id"] for player in active_players]
    return player_ids

async def fetch_all_players_game_logs(player_ids: list[int], season_year: str):
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for player_id in tqdm(player_ids, desc="Fetching Player Game Logs"):
            task = tg.create_task(fetch_data_async(fetch_player_game_logs, player_id, season_year))
            tasks.append(task)
            await asyncio.sleep(0.600)

    results = [await task for task in tasks]

    return results

async def main():
    player_ids = get_all_player_ids()

    all_players_game_logs = await fetch_all_players_game_logs(player_ids, '2023-24')

    print(all_players_game_logs)

if __name__ == "__main__":
    asyncio.run(main())
