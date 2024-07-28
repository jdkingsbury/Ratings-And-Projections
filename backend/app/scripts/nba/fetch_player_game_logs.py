import asyncio
from datetime import datetime

import pandas as pd
from app.db.database import async_engine
from app.db.models.sports.nba import NBAGameLog
from app.utils.fetch_utils import fetch_data_async
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from sqlalchemy.ext.asyncio import AsyncSession
from tqdm.asyncio import tqdm

# TODO: Need to include season_year as a column


# Function to fetch player game logs
# NOTE: The season_year parameter will take a string that looks like this: 2023-24
def fetch_player_game_logs(player_id: int, season_year: str) -> pd.DataFrame:
    player_game_log = playergamelog.PlayerGameLog(
        player_id=player_id, season=season_year
    )
    player_game_log_df = player_game_log.get_data_frames()[0]

    # Returns an empty DataFrame if no game logs are found
    if player_game_log_df.empty:
        return pd.DataFrame()

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
            "FG3A": "fg3a",
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
    # Convert game_date from string to datetime.date
    player_game_log_df["game_date"] = player_game_log_df["game_date"].apply(
        lambda x: datetime.strptime(x, "%b %d, %Y").date()
    )

    # Convert to true or false
    player_game_log_df["video_available"] = player_game_log_df["video_available"].apply(
        lambda x: x == 1
    )

    # Convert game_id to a string
    player_game_log_df["game_id"] = player_game_log_df["game_id"].astype(str)

    # Add season_year as a column
    player_game_log_df["season_year"] = season_year

    return player_game_log_df


# Function to get all active players IDs
def get_all_player_ids() -> list[int]:
    all_players = players.get_players()
    active_players = [player for player in all_players if player["is_active"]]
    player_ids = [player["id"] for player in active_players]
    return player_ids


async def fetch_all_players_game_logs(
    player_ids: list[int], season_year: str
) -> list[pd.DataFrame]:
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for player_id in tqdm(player_ids, desc="Fetching Player Game Logs"):
            task = tg.create_task(
                fetch_data_async(fetch_player_game_logs, player_id, season_year)
            )
            tasks.append(task)
            await asyncio.sleep(0.600)

    results = [await task for task in tasks]

    return results


# Function to insert all player game logs
async def insert_all_player_game_logs(player_game_logs_dfs: list[pd.DataFrame]):
    async with AsyncSession(async_engine) as session:
        async with session.begin():
            with session.no_autoflush:
                for player_game_logs_df in tqdm(
                    player_game_logs_dfs, desc="Inserting Players Game Logs"
                ):
                    if player_game_logs_df.empty:
                        print(f"No game logs found. Skipping.")
                        continue

                    player_game_log_dicts = player_game_logs_df.to_dict(
                        orient="records"
                    )

                    for player_game_log_dict in player_game_log_dicts:
                        game_logs = NBAGameLog(**player_game_log_dict)
                        await session.merge(game_logs)

        await session.commit()


async def main() -> None:
    # Collect all the active player ids
    player_ids = get_all_player_ids()

    # Collect all the DataFrames of all the player game logs fetched
    all_players_game_logs_dfs = await fetch_all_players_game_logs(player_ids, "2023-24")

    # Insert all player game logs into the database
    await insert_all_player_game_logs(all_players_game_logs_dfs)

    print("Data Inserted Successfully!")


if __name__ == "__main__":
    asyncio.run(main())
