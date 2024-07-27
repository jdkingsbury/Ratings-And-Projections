from app.db.models.sports.nba import NBAPlayer
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_players(db: Session):
    return db.execute(select(NBAPlayer)).scalars().all()


def get_player_info(db: Session, player_id: int):
    return db.execute(select(NBAPlayer).filter(NBAPlayer.player_id == player_id)).scalar()
