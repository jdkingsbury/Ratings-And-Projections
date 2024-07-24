import asyncio

from app.scripts.nba.fetch_players import main as fetch_nba_players


# Calls other scripts to populate the database
async def populate_db():
    await fetch_nba_players()


if __name__ == "__main__":
    asyncio.run(populate_db())
