import asyncio
from typing import List

import pandas as pd
from app.db.database import SessionLocal
from app.db.models.league import League
from app.db.models.sports.nba import NBACareerStats
from app.utils.fetch_utils import fetch_data_async
from app.utils.player_utils import fetch_all_player_ids_nba as fetch_all_player_ids
from nba_api.stats.endpoints import playercareerstats
from sqlalchemy.exc import SQLAlchemyError
from tqdm.asyncio import tqdm


# Synchronous function to fetch nba players career stats
def fetch_player_career_stats(player_id: int) -> pd.DataFrame:
    player_career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    player_career_stats_df = player_career_stats.get_data_frames()[0]

    if player_career_stats_df.empty:
        return pd.DataFrame()

    player_career_stats_df = player_career_stats_df.rename(
        columns={
            "PLAYER_ID": "player_id",
            "SEASON_ID": "season_id",
            # NOTE: League_id column will need to be changed to use ours
            "LEAGUE_ID": "league_id",
            "TEAM_ID": "team_id",
            "TEAM_ABBREVIATION": "team_abbreviation",
            "PLAYER_AGE": "player_age",
            "GP": "gp",
            "GS": "gs",
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
        }
    )

    return player_career_stats_df


# function to fetch career stats for each player
async def fetch_all_players_career_stats(player_ids: List[int]) -> List[pd.DataFrame]:
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for player_id in tqdm(player_ids, desc="Fetching Players Career Stats"):
            task = tg.create_task(
                fetch_data_async(fetch_player_career_stats, player_id)
            )
            tasks.append(task)
            await asyncio.sleep(0.600)

    results = [await task for task in tasks]

    return results


# FIX: Determine what to do when the team_id is 0. May need to reference or edit the model.


# function to insert all players career stats into the database
def insert_all_players_career_stats(
    merged_players_career_stats_df: pd.DataFrame, league_id: int
) -> None:
    with SessionLocal() as session:
        try:
            for _, row in tqdm(
                merged_players_career_stats_df.iterrows(),
                desc="Inserting players career stats into the database",
            ):
                career_stats = NBACareerStats(
                    player_id=row["player_id"],
                    season_id=row["season_id"],
                    league_id=league_id,
                    team_id=row["team_id"],
                    team_abbreviation=row["team_abbreviation"],
                    player_age=row["player_age"],
                    gp=row["gp"],
                    gs=row["gs"],
                    min=row["min"],
                    fgm=row["fgm"],
                    fga=row["fga"],
                    fg_pct=row["fg_pct"],
                    fg3m=row["fg3m"],
                    fg3a=row["fg3a"],
                    fg3_pct=row["fg3_pct"],
                    ftm=row["ftm"],
                    fta=row["fta"],
                    ft_pct=row["ft_pct"],
                    oreb=row["oreb"],
                    dreb=row["dreb"],
                    reb=row["reb"],
                    ast=row["ast"],
                    stl=row["stl"],
                    blk=row["blk"],
                    tov=row["tov"],
                    pf=row["pf"],
                    pts=row["pts"],
                )
                session.merge(career_stats)
            print("Successfully Inserted Players Career Stats Into the Database")
            session.flush()
            session.commit()

        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error inserting players career stats: {e}")
        finally:
            session.close()


async def main() -> None:
    with SessionLocal() as session:
        try:
            # Fetch league ID for NBA from the database
            nba_league = session.query(League).filter_by(name="NBA").one_or_none()
            if nba_league is None:
                print("NBA league is not found!")
                return

            league_id = nba_league.id
            if not isinstance(league_id, int):
                raise TypeError("League ID should be an integer")

            # Collect all player ids
            player_ids = fetch_all_player_ids()

            # Collect all players career stats dataframes
            all_players_career_stats_dfs = await fetch_all_players_career_stats(
                player_ids
            )

            # Combine all players career stats dataframes
            merged_players_career_stats_df = pd.concat(all_players_career_stats_dfs)

            # NOTE: Used for debugging purposes. Discovered that when team_id is 0 might be linked to the player playing for multiple teams due to the team abbreviation TOT.
            merged_players_career_stats_df.to_json(
                f"/app/output/players_career_stats.json", orient="records", index=False
            )

            # insert_all_players_career_stats(merged_players_career_stats_df, league_id)

        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error: {e}")

        finally:
            session.close()


if __name__ == "__main__":
    asyncio.run(main())
