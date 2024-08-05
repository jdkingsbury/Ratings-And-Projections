from typing import List, Optional

from app.db.models.sports.nba import NBAGameLog, NBAPlayer, NBATeam
from sqlalchemy import select
from sqlalchemy.orm import Session


def fetch_players(db: Session) -> List[NBAPlayer]:
    """Fetches all NBA Players from the database."""
    return list(db.execute(select(NBAPlayer)).scalars().all())


def fetch_player_info(db: Session, player_id: int) -> Optional[NBAPlayer]:
    """Fetches information of a specific NBA player by player_id."""
    return db.execute(
        select(NBAPlayer).filter(NBAPlayer.player_id == player_id)
    ).scalar()


def fetch_last_five_games_for_player(db: Session, player_id: int, season_year: str):
    """Fetches the last 5 games for a specific NBA player."""
    return (
        db.execute(
            select(NBAGameLog)
            .filter(NBAGameLog.player_id == player_id)
            .filter(NBAGameLog.season_year == season_year)
            .order_by(NBAGameLog.game_date.desc())
            .limit(5)
        )
        .scalars()
        .all()
    )

def fetch_teams(db: Session) -> List[NBATeam]:
    """Fetches all NBA Teams from the database"""
    return list(db.execute(select(NBATeam)).scalars().all())
