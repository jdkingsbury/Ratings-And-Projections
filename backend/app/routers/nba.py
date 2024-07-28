from typing import List, Optional

from app.db.database import SessionLocal
from app.schemas.nba import NBAGameLogBase, NBAPlayerBase
from app.services.nba_service import (
    get_last_five_games_for_player,
    get_player_info,
    get_players,
)
from app.utils.current_nba_season import get_current_season_year
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/nba", tags=["nba"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/players", response_model=List[NBAPlayerBase])
def get_all_players(db: Session = Depends(get_db)):
    player = get_players(db)
    if not player:
        raise HTTPException(status_code=404, detail="No players found")
    return player


@router.get("/players/{player_id}", response_model=Optional[NBAPlayerBase])
def get_player(player_id: int, db: Session = Depends(get_db)):
    player = get_player_info(db, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.get("/players/{player_id}/recent_games", response_model=List[NBAGameLogBase])
def get_last_five_games(
    player_id: int,
    season_year: str = Depends(get_current_season_year),
    db: Session = Depends(get_db),
):
    games = get_last_five_games_for_player(db, player_id, season_year)
    if not games:
        raise HTTPException(
            status_code=404, detail="No recent games were found for this player"
        )
    return games
