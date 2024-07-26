from app.db.models.nba.models import Player
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_players(db: Session):
    return db.execute(select(Player)).scalars().all()


def get_player_info(db: Session, player_id: int):
    return db.execute(select(Player).filter(Player.player_id == player_id)).scalar()
