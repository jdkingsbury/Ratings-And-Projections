from sqlalchemy.orm import Session
from app.models.player_model import Player
from app.schemas.player_schema import PlayerCreate, PlayerUpdate 

def create_player(db: Session, player: PlayerCreate):
    # ** used to upack dicts key value pairs
    db_player = Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_active_players(db: Session):
    return db.query(Player).filter(Player.is_active == True).all()
