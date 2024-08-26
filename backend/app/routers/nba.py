from typing import List, Optional

from app.db.database import SessionLocal
from app.schemas.nba import (
    NBAGameLogBase,
    NBAPlayerBase,
    NBAPlayerCardInfo,
    NBATeamBase,
)
from app.services.nba_service import (
    fetch_last_five_games_for_player,
    fetch_player_card_info,
    fetch_player_info,
    fetch_players,
    fetch_teams,
)
from app.utils.nba_utils import get_current_season_year
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/nba", tags=["nba"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/players/{player_id}/player_card", response_model=Optional[NBAPlayerCardInfo]
)
def fetch_player_card(player_id: int, db: Session = Depends(get_db)):
    player = fetch_player_card_info(db, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.get("/players", response_model=List[NBAPlayerBase])
def fetch_all_players(db: Session = Depends(get_db)):
    players = fetch_players(db)
    if not players:
        raise HTTPException(status_code=404, detail="No players found")
    return players


@router.get("/players/{player_id}", response_model=Optional[NBAPlayerBase])
def fetch_player(player_id: int, db: Session = Depends(get_db)):
    player = fetch_player_info(db, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.get("/players/{player_id}/recent_games", response_model=List[NBAGameLogBase])
def fetch_last_five_games(
    player_id: int,
    season_year: str = Depends(get_current_season_year),
    db: Session = Depends(get_db),
):
    games = fetch_last_five_games_for_player(db, player_id, season_year)
    if not games:
        raise HTTPException(
            status_code=404, detail="No recent games were found for this player"
        )
    return games


@router.get("/teams", response_model=List[NBATeamBase])
def fetch_all_teams(db: Session = Depends(get_db)):
    teams = fetch_teams(db)
    if not teams:
        raise HTTPException(status_code=404, detail="No teams found")
    return teams
