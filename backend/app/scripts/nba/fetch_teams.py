import pandas as pd
from app.db.database import SessionLocal
from app.db.models.league import League
from app.db.models.sports.nba import NBATeam
from nba_api.stats.static import teams
from sqlalchemy.exc import SQLAlchemyError


# Fetch all the NBA teams
def fetch_all_teams() -> pd.DataFrame:
    all_teams = teams.get_teams()
    all_teams_df = pd.DataFrame(all_teams)
    all_teams_df = all_teams_df[
        [
            "id",
            "full_name",
            "abbreviation",
            "nickname",
            "city",
            "state",
        ]
    ]

    if not isinstance(all_teams_df, pd.DataFrame):
        raise TypeError("The function fetch_all_teams must return a pandas DataFrame")

    return all_teams_df


# Insert all the nba teams
def insert_all_teams(all_teams_df: pd.DataFrame, league_id: int) -> None:
    with SessionLocal() as session:
        try:
            for _, row in all_teams_df.iterrows():
                team = NBATeam(
                    id=row["id"],
                    full_name=row["full_name"],
                    abbreviation=row["abbreviation"],
                    nickname=row["nickname"],
                    city=row["city"],
                    state=row["state"],
                    league_id=league_id,
                )
                session.merge(team)
            print("Successfully Inserted NBA Teams Into The Database!")
            session.flush()
            session.commit()

        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error inserting teams: {e}")

        finally:
            session.close()


def main() -> None:
    with SessionLocal() as session:
        try:
            # Fetch the League Id for NBA
            nba_league = session.query(League).filter_by(name="NBA").one_or_none()
            if nba_league is None:
                print("NBA league not found!")
                return

            league_id = nba_league.id
            if not isinstance(league_id, int):
                raise TypeError("League ID should be an integer")

            all_teams_df = fetch_all_teams()
            insert_all_teams(all_teams_df, league_id)

        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error: {e}")

        finally:
            session.close()
