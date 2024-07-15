from app.database import SessionLocal
from app.models.player_model import Player
from app.schemas.player_schema import PlayerCreate
from app.services.nba_service import fetch_all_players

def populate_players():
    session = SessionLocal()
    players_data = fetch_all_players()

    for player_data in players_data:
        player_create = PlayerCreate(**player_data)
        db_player = Player(**player_create.dict())
        session.add(db_player)

    session.commit()
    session.close()
    
if __name__ == "__main__":
    populate_players()
