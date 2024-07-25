import asyncio

import pandas as pd
from app.db.database import async_engine
from app.db.models.models import Player
from app.utils.fetch_utils import fetch_data_async
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
from sqlalchemy.ext.asyncio import AsyncSession
from tqdm.asyncio import tqdm


# Synchronous function to fetch nba player info
def fetch_player_info(player_id):
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
    player_info_df["image_url"] = player_info_df["player_id"].apply(
        lambda x: f"https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{x}.png"
    )

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
            "image_url",
        ]
    ]

    return player_info_df


# Function to get all active players IDs
def get_all_player_ids():
    all_players = players.get_players()
    active_players = [player for player in all_players if player["is_active"]]
    player_ids = [player["id"] for player in active_players]
    return player_ids


async def fetch_all_players_info(player_ids):
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for player_id in tqdm(player_ids, desc="Fetching Player Info"):
            task = tg.create_task(fetch_data_async(fetch_player_info, player_id))
            tasks.append(task)
            await asyncio.sleep(0.600) 

    results = [await task for task in tasks]

    return results

# FIX: Receiving an error where the team_id isn't matching the id in the teams table
async def insert_all_player_info(player_info_dfs):
    async with AsyncSession(async_engine) as session:
        async with session.begin():
            with session.no_autoflush:
                for player_info_df in tqdm(
                    player_info_dfs, desc="Inserting Players Into Player DB"
                ):
                    player_info_dict = player_info_df.to_dict(orient="records")[0]
                    player = Player(**player_info_dict)
                    await session.merge(player)

        await session.commit()


async def main():
    # Collect all the active player ids
    player_ids = get_all_player_ids()

    # Collect all the DataFrames of all the players fetched
    all_players_info_dfs = await fetch_all_players_info(player_ids)

    # Insert all players info into a database
    await insert_all_player_info(all_players_info_dfs)


if __name__ == "__main__":
    asyncio.run(main())
