from typing import Dict, List

from app.db.database import SessionLocal
from app.db.models.league import League
from app.db.models.sport import Sport


def insert_sports() -> None:

    sports_data: List[Dict[str, str]] = [
        {"name": "Basketball"},
        {"name": "Football"},
        {"name": "Baseball"},
    ]

    with SessionLocal() as session:
        try:
            # Inserts Sports Data
            sports_instances = [Sport(**sport) for sport in sports_data]
            session.bulk_save_objects(sports_instances)
            session.flush()
            print("Successfully Inserted Sports Data!")
            session.commit()

        except Exception as e:
            session.rollback()
            print(f"Error inserting sports data: {e}")

        finally:
            session.close()


def insert_leagues() -> None:

    leagues_data: Dict[str, List[Dict[str, str]]] = {
        "Basketball": [{"name": "NBA"}],
        "Football": [{"name": "NFL"}],
        "Baseball": [{"name": "MLB"}],
    }

    with SessionLocal() as session:
        try:
            sports_instances: List[Sport] = session.query(Sport).all()

            # Insert Leagues Data
            for sport in sports_instances:
                if sport.name in leagues_data:
                    league_instances = [
                        League(name=league["name"], sport_id=sport.id)
                        for league in leagues_data[sport.name]
                    ]
                    session.bulk_save_objects(league_instances)

            session.flush()
            session.commit()
            print("Successfully Inserted Sports And Leagues Data!")

        except Exception as e:
            session.rollback()
            print(f"Error to insert data: {e}")

        finally:
            session.close()


def main() -> None:
    insert_sports()
    insert_leagues()
