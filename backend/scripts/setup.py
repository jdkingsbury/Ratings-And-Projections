from app.database import SessionLocal, create_tables
from app.models.player_model import Player
from app.schemas.player_schema import PlayerCreate
from sqlalchemy.orm import Session
from app.services.nba_service import fetch_all_players


def init_db():
    create_tables()
    print("here")
    db: Session = SessionLocal()

    try:
        if not db.query(Player).first():
            players_data = fetch_all_players()
            for player_data in players_data:
                player_create = PlayerCreate(**player_data)
                db_player = Player(**player_create.dict())
                db.add(db_player)
            db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
