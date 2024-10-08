import asyncio
from typing import List

import pandas as pd
from app.db.database import SessionLocal
from app.db.models.league import League
from app.utils.fetch_utils import fetch_data_async
from nba_api.stats.endpoints import teaminfocommon
from nba_api.stats.static import teams
from sqlalchemy import text
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
            "full_name": "name",
            "abbreviation": "abbreviation",
            "nickname": "nickname",
            "city": "city",
            "state": "state",
            "year_founded": "year_founded",
        }
    )

    return all_teams_df


def insert_all_teams(combined_teams_df: pd.DataFrame, league_id: int) -> None:
    with SessionLocal() as session:
        try:
            insert_query = text(
                """
                INSERT INTO nba_teams (
                    team_id, name, abbreviation, nickname, city, state,
                    conference, division, year_founded, w, l, pct, conf_rank,
                    div_rank, season_year, league_id
                ) VALUES (
                    :team_id, :name, :abbreviation, :nickname, :city, :state,
                    :conference, :division, :year_founded, :w, :l, :pct, :conf_rank,
                    :div_rank, :season_year, :league_id
                )
                ON CONFLICT (team_id) DO UPDATE SET
                    name = excluded.name,
                    abbreviation = excluded.abbreviation,
                    nickname = excluded.nickname,
                    city = excluded.city,
                    state = excluded.state,
                    conference = excluded.conference,
                    division = excluded.division,
                    year_founded = excluded.year_founded,
                    w = excluded.w,
                    l = excluded.l,
                    pct = excluded.pct,
                    conf_rank = excluded.conf_rank,
                    div_rank = excluded.div_rank,
                    season_year = excluded.season_year,
                    league_id = excluded.league_id
            """
            )
            for _, row in tqdm(
                combined_teams_df.iterrows(), desc="Inserting teams into the database"
            ):
                session.execute(
                    insert_query,
                    {
                        "team_id": row["team_id"],
                        "name": row["name"],
                        "abbreviation": row["abbreviation"],
                        "nickname": row["nickname"],
                        "city": row["city"],
                        "state": row["state"],
                        "conference": row.get(
                            "conference", None
                        ),  # Handling possible missing values
                        "division": row.get("division", None),
                        "year_founded": row.get("year_founded", None),
                        "w": row.get("w", None),
                        "l": row.get("l", None),
                        "pct": row.get("pct", None),
                        "conf_rank": row.get("conf_rank", None),
                        "div_rank": row.get("div_rank", None),
                        "season_year": row.get("season_year", None),
                        "league_id": league_id,
                    },
                )
            print("Successfully Inserted NBA Teams Into the Database")
            session.commit()

        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error inserting teams: {e}")

        finally:
            session.close()


async def main() -> None:

    with SessionLocal() as session:
        try:
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
