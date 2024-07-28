import asyncio

from app.db.database import Base, engine
from app.scripts.core import main as insert_sports_and_leagues
from app.scripts.nba.fetch_player_game_logs import main as fetch_nba_player_game_logs
from app.scripts.nba.fetch_players import main as fetch_nba_players
from app.scripts.nba.fetch_teams import main as fetch_nba_teams


def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables Successfully Created!")
    except Exception as e:
        print(f"Error creating tables: {e}")
    return


# Calls other scripts to populate the database
async def populate_db():
    try:
        insert_sports_and_leagues()
        fetch_nba_teams()
        await fetch_nba_players()
        await fetch_nba_player_game_logs()
        print("Database Successfully Populated!")
    except Exception as e:
        print(f"Error populating database as {e}")


if __name__ == "__main__":
    create_tables()
    asyncio.run(populate_db())
