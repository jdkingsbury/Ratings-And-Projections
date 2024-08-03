import asyncio
from typing import List

import pandas as pd
from app.utils.fetch_utils import fetch_data_async
from nba_api.stats.endpoints import teaminfocommon
from nba_api.stats.static import teams
from tqdm.asyncio import tqdm


# Synchronous function to fetch nba teams info
def fetch_team_info(team_id: int) -> pd.DataFrame:
    team_info = teaminfocommon.TeamInfoCommon(team_id=team_id)

    team_info_df = team_info.get_data_frames()[0]
    team_info_df = team_info_df.rename(
        columns={
            "TEAM_ID": "team_id",
            "SEASON_YEAR": "season_year",
            "TEAM_CITY": "team_city",
            "TEAM_NAME": "team_name",
            "TEAM_ABBREVIATION": "team_abbreviation",
            "TEAM_CONFERENCE": "team_conference",
            "TEAM_DIVISION": "team_division",
            "W": "w",
            "L": "l",
            "PCT": "pct",
            "CONF_RANK": "conf_rank",
            "DIV_RANK": "div_rank",
        }
    )

    return team_info_df


def fetch_all_team_ids() -> List[int]:
    all_teams = teams.get_teams()
    team_ids = [team["id"] for team in all_teams]
    return team_ids


async def fetch_all_teams_info(team_ids: List[int]) -> List[pd.DataFrame]:
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for team_id in tqdm(team_ids, desc="Fetching Team Info"):
            task = tg.create_task(fetch_data_async(fetch_team_info, team_id))
            tasks.append(task)
            await asyncio.sleep(0.600)

    results = [await task for task in tasks]

    return results


def fetch_all_teams() -> pd.DataFrame:
    all_teams = teams.get_teams()
    all_teams_df = pd.DataFrame(all_teams)

    all_teams_df = all_teams_df.rename(
        columns={
            "id": "team_id",
            "full_name": "team_name",
            "abbreviation": "team_abbreviation",
            "nickname": "team_nickname",
            "city": "team_city",
            "state": "team_state",
        }
    )

    return all_teams_df


async def main() -> None:
    # Collect all team ids
    team_ids = fetch_all_team_ids()

    # Collect all team info dataframes
    all_teams_info_dfs = await fetch_all_teams_info(team_ids)

    # Combine all team infos dataframes
    detailed_team_info = pd.concat(all_teams_info_dfs, ignore_index=True)

    # Fetch all teams from the nba_api static function
    basic_team_info = fetch_all_teams()

    combined_teams_df = pd.merge(
        detailed_team_info, basic_team_info, on="team_id", how="inner"
    )


if __name__ == "__main__":
    asyncio.run(main())
