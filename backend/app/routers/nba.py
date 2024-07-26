from app.db.database import SessionLocal
from app.services.nba_service import *
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/nba", tags=["nba"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/players")
def get_all_players(db: Session = Depends(get_db)):
    player = get_players(db)
    if not player:
        raise HTTPException(status_code=404, detail="No players found")
    return player


@router.get("/players/{player_id}")
def retrieve_player(player_id: int, db: Session = Depends(get_db)):
    player = get_player_info(db, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player
