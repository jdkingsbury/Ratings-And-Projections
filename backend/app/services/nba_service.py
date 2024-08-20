from typing import List, Optional

from app.db.database import SessionLocal
from app.db.models.sports.nba import NBAGameLog, NBAPlayer, NBATeam
from app.utils.nba_utils import fetch_players_team
from sqlalchemy import select
from sqlalchemy.orm import Session


def fetch_player_card_info(db: Session, player_id: int) -> Optional[dict]:
    """Fetches NBA Player Card Info """
    query = select(
        NBAPlayer.player_id,
        NBAPlayer.first_last,
        NBAPlayer.team_id,
        NBAPlayer.image_url,
    ).filter(NBAPlayer.player_id == player_id)

    result = db.execute(query).fetchone()

    if result:
        result_dict = {
            "player_id": result[0],
            "first_last": result[1],
            "team_id": result[2],
            "image_url": result[3],
        }

        team_id = result_dict["team_id"]

        team_name = fetch_players_team(team_id)

        result_dict["team_name"] = team_name

        del result_dict["team_id"]

        return result_dict

    return None


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


if __name__ == "__main__":
    db = SessionLocal()
    try:
        player_id = 2544

        fetch_player_card_info(db, player_id)
    finally:
        db.close()
