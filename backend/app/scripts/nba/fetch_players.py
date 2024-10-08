import asyncio
from datetime import datetime
from typing import List

import pandas as pd
from app.db.database import async_engine
from app.utils.fetch_utils import fetch_data_async
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from tqdm.asyncio import tqdm


# Synchronous function to fetch nba player info
def fetch_player_info(player_id: int) -> pd.DataFrame:
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)

    player_info_df = player_info.get_data_frames()[0]
    player_info_df = player_info_df.rename(
        columns={
            "PERSON_ID": "player_id",
            "DISPLAY_FIRST_LAST": "first_last",
            "FIRST_NAME": "first_name",
            "LAST_NAME": "last_name",
            "BIRTHDATE": "birth_date",
            "SCHOOL": "school",
            "COUNTRY": "country",
            "HEIGHT": "height",
            "WEIGHT": "weight",
            "JERSEY": "jersey",
            "POSITION": "position",
            "ROSTERSTATUS": "is_active",
            "TEAM_ID": "team_id",
            "FROM_YEAR": "from_year",
            "TO_YEAR": "to_year",
            "DRAFT_YEAR": "draft_year",
            "DRAFT_ROUND": "draft_round",
            "DRAFT_NUMBER": "draft_number",
        }
    )

    # Convert to true or false
    player_info_df["is_active"] = player_info_df["is_active"].apply(
        lambda x: x == "Active"
    )

    player_info_df = player_info_df[
        [
            "player_id",
            "first_last",
            "first_name",
            "last_name",
            "birth_date",
            "school",
            "country",
            "height",
            "weight",
            "jersey",
            "position",
            "is_active",
            "team_id",
            "from_year",
            "to_year",
            "draft_year",
            "draft_round",
            "draft_number",
        ]
    ]

    return player_info_df


# Function to get all active players IDs
def fetch_all_player_ids() -> List[int]:
    all_players = players.get_players()
    active_players = [player for player in all_players if player["is_active"]]
    player_ids = [player["id"] for player in active_players]
    return player_ids


# Function calls fetch data async and creates a task to fetch player info for each player_id
async def fetch_all_players_info(player_ids: list[int]) -> List[pd.DataFrame]:
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for player_id in tqdm(player_ids, desc="Fetching Player Info"):
            task = tg.create_task(fetch_data_async(fetch_player_info, player_id))
            tasks.append(task)
            await asyncio.sleep(0.600)

    results = [await task for task in tasks]

    return results


# Asynchronous function to inset player information
async def insert_all_player_info(player_info_dfs: List[pd.DataFrame]):
    async with AsyncSession(async_engine) as session:
        async with session.begin():
            with session.no_autoflush:
                for player_info_df in tqdm(
                    player_info_dfs, desc="Inserting Players Into Player DB"
                ):
                    player_info_dict = player_info_df.to_dict(orient="records")[0]
                    team_id = player_info_dict.get("team_id")

                    # Convert birth_date to string in ISO format
                    if isinstance(player_info_dict.get("birth_date"), str):
                        try:
                            player_info_dict["birth_date"] = datetime.fromisoformat(
                                player_info_dict["birth_date"]
                            ).date()
                        except ValueError:
                            print(
                                f"Error parsing date: {player_info_dict.get('birth_date')}. Skipping."
                            )
                            continue

                    # Check if the player is part of a team
                    if team_id == 0 or team_id is None:
                        print(
                            f"Invalid Team ID {team_id} for player {player_info_dict.get('first_last')}. Setting to None."
                        )
                        player_info_dict["team_id"] = None

                    else:

                        result = await session.execute(
                            text("SELECT * FROM nba_teams WHERE team_id = :team_id"),
                            {"team_id": team_id},
                        )
                        team_exists = result.fetchone()

                        # Check if the team id tied to the player is valid
                        if not team_exists:
                            print(
                                f"Team ID {team_id} not found for player {player_info_dict.get('first_last')}. Setting to None."
                            )
                            player_info_dict["team_id"] = None

                    insert_statement = text(
                        """
                        INSERT INTO nba_players (
                            player_id, first_last, first_name, last_name, birth_date,
                            school, country, height, weight, jersey, position,
                            is_active, team_id, from_year, to_year, draft_year,
                            draft_round, draft_number
                        ) VALUES (
                            :player_id, :first_last, :first_name, :last_name, :birth_date,
                            :school, :country, :height, :weight, :jersey, :position,
                            :is_active, :team_id, :from_year, :to_year, :draft_year,
                            :draft_round, :draft_number
                        ) ON CONFLICT (player_id) DO UPDATE SET
                            first_last = EXCLUDED.first_last,
                            first_name = EXCLUDED.first_name,
                            last_name = EXCLUDED.last_name,
                            birth_date = EXCLUDED.birth_date,
                            school = EXCLUDED.school,
                            country = EXCLUDED.country,
                            height = EXCLUDED.height,
                            weight = EXCLUDED.weight,
                            jersey = EXCLUDED.jersey,
                            position = EXCLUDED.position,
                            is_active = EXCLUDED.is_active,
                            team_id = EXCLUDED.team_id,
                            from_year = EXCLUDED.from_year,
                            to_year = EXCLUDED.to_year,
                            draft_year = EXCLUDED.draft_year,
                            draft_round = EXCLUDED.draft_round,
                            draft_number = EXCLUDED.draft_number
                    """
                    )
                    await session.execute(insert_statement, player_info_dict)

        await session.commit()


async def main() -> None:
    # Collect all the active player ids
    player_ids = fetch_all_player_ids()

    # Collect all the DataFrames of all the players fetched
    all_players_info_dfs = await fetch_all_players_info(player_ids)

    # Insert all players info into a database
    await insert_all_player_info(all_players_info_dfs)
