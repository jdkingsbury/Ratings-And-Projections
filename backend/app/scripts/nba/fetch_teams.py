import asyncio
from typing import List

import pandas as pd
from app.db.database import SessionLocal
from app.db.models.league import League
from app.db.models.sports.nba import NBATeam
from app.utils.fetch_utils import fetch_data_async
from app.utils.team_utils import fetch_all_team_ids_nba as fetch_all_team_ids
from nba_api.stats.endpoints import teaminfocommon
from nba_api.stats.static import teams
from sqlalchemy.exc import SQLAlchemyError
from tqdm.asyncio import tqdm


# Synchronous function to fetch nba teams info
def fetch_team_info(team_id: int) -> pd.DataFrame:
    team_info = teaminfocommon.TeamInfoCommon(team_id=team_id)

    team_info_df = team_info.get_data_frames()[0]
    team_info_df = team_info_df.rename(
        columns={
            "TEAM_ID": "team_id",
            "SEASON_YEAR": "season_year",
            "TEAM_CITY": "city",
            "TEAM_NAME": "name",
            "TEAM_ABBREVIATION": "abbreviation",
            "TEAM_CONFERENCE": "conference",
            "TEAM_DIVISION": "division",
            "W": "w",
            "L": "l",
            "PCT": "pct",
            "CONF_RANK": "conf_rank",
            "DIV_RANK": "div_rank",
        }
    )

    return team_info_df


# function to fetch team info for each team
async def fetch_all_teams_info(team_ids: List[int]) -> List[pd.DataFrame]:
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for team_id in tqdm(team_ids, desc="Fetching Team Info"):
            task = tg.create_task(fetch_data_async(fetch_team_info, team_id))
            tasks.append(task)
            await asyncio.sleep(0.600)

    results = [await task for task in tasks]

    return results


# function to fetch all teams using the nba_api static function
def fetch_all_teams() -> pd.DataFrame:
    all_teams = teams.get_teams()
    all_teams_df = pd.DataFrame(all_teams)

    all_teams_df = all_teams_df.rename(
        columns={
            "id": "team_id",
            "full_name": "name",
            "abbreviation": "abbreviation",
            "nickname": "nickname",
            "city": "city",
            "state": "state",
            "year_founded": "year_founded",
        }
    )

    return all_teams_df


# function to insert all teams into the database
def insert_all_teams(combined_teams_df: pd.DataFrame, league_id: int) -> None:
    with SessionLocal() as session:
        try:
            for _, row in tqdm(
                combined_teams_df.iterrows(), desc="Inserting teams into the database"
            ):
                team = NBATeam(
                    team_id=row["team_id"],
                    name=row["name"],
                    abbreviation=row["abbreviation"],
                    nickname=row["nickname"],
                    city=row["city"],
                    state=row["state"],
                    conference=row["conference"],
                    division=row["division"],
                    year_founded=row["year_founded"],
                    w=row["w"],
                    l=row["l"],
                    pct=row["pct"],
                    conf_rank=row["conf_rank"],
                    div_rank=row["div_rank"],
                    season_year=row["season_year"],
                    league_id=league_id,
                )
                session.merge(team)
            print("Successfully Inserted NBA Teams Into the Database")
            session.flush()
            session.commit()

        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error inserting teams: {e}")

        finally:
            session.close()


async def main() -> None:

    with SessionLocal() as session:
        try:
            # Fetch league ID for NBA from the database
            nba_league = session.query(League).filter_by(name="NBA").one_or_none()
            if nba_league is None:
                print("NBA league not found!")
                return

            league_id = nba_league.id
            if not isinstance(league_id, int):
                raise TypeError("League ID should be an integer")

            # Collect all team ids
            team_ids = fetch_all_team_ids()

            # Collect all team info dataframes
            all_teams_info_dfs = await fetch_all_teams_info(team_ids)

            # Combine all team infos dataframes
            detailed_team_info = pd.concat(all_teams_info_dfs, ignore_index=True)

            # Fetch all teams from the nba_api static function
            basic_team_info = fetch_all_teams()

            # Combine the two dataframes
            combined_teams_df = basic_team_info.combine_first(detailed_team_info)

            # Inserts all the teams and team data into the database
            insert_all_teams(combined_teams_df, league_id)

        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error: {e}")

        finally:
            session.close()


if __name__ == "__main__":
    asyncio.run(main())
