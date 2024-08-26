from typing import List, Optional

from app.db.database import SessionLocal
from app.db.models.sports.nba import NBAGameLog, NBAPlayer, NBATeam
from app.utils.nba_utils import fetch_players_team
from sqlalchemy import select
from sqlalchemy.orm import Session


def fetch_player_card_info(db: Session, player_id: int) -> Optional[dict]:
    """Fetches NBA Player Card Info"""
    query = select(
        NBAPlayer.player_id,
        NBAPlayer.first_last,
        NBAPlayer.team_id,
        NBAPlayer.image_url,
    ).filter(NBAPlayer.player_id == player_id)

    result = db.execute(query).fetchone()

    if result:
        card_data = {
            "player_id": result[0],
            "first_last": result[1],
            "team_id": result[2],
            "image_url": result[3],
        }

        team_id = card_data["team_id"]

        team_name = fetch_players_team(team_id)

        card_data["team_name"] = team_name

        del card_data["team_id"]

        return card_data

    return None


# TODO: Fetch each players team name
def fetch_players(db: Session) -> List[dict]:
    """Fetches all NBA Players from the database."""
    query = select(NBAPlayer)

    players = db.execute(query).scalars().all()

    players_with_team_names = []

    for player in players:
        player_data = {
            "player_id": player.player_id,
            "first_last": player.first_last,
            "first_name": player.first_name,
            "last_name": player.last_name,
            "birth_date": player.birth_date,
            "school": player.school,
            "country": player.country,
            "height": player.height,
            "weight": player.weight,
            "jersey": player.jersey,
            "position": player.position,
            "is_active": player.is_active,
            "team_id": player.team_id,
            "from_year": player.from_year,
            "to_year": player.to_year,
            "draft_year": player.draft_year,
            "draft_round": player.draft_round,
            "draft_number": player.draft_number,
            "image_url": player.image_url,
        }

        team_id = player_data["team_id"]

        team_name = fetch_players_team(team_id) if team_id else None

        player_data["team_name"] = team_name

        players_with_team_names.append(player_data)

    return players_with_team_names


def fetch_player_info(db: Session, player_id: int) -> Optional[dict]:
    """Fetches information of a specific NBA player by player_id."""
    query = select(NBAPlayer).filter(NBAPlayer.player_id == player_id)

    result = db.execute(query).fetchone()

    if result and isinstance(result[0], NBAPlayer):
        player = result[0]

        player_data = {
            "player_id": player.player_id,
            "first_last": player.first_last,
            "first_name": player.first_name,
            "last_name": player.last_name,
            "birth_date": player.birth_date,
            "school": player.school,
            "country": player.country,
            "height": player.height,
            "weight": player.weight,
            "jersey": player.jersey,
            "position": player.position,
            "is_active": player.is_active,
            "team_id": player.team_id,
            "from_year": player.from_year,
            "to_year": player.to_year,
            "draft_year": player.draft_year,
            "draft_round": player.draft_round,
            "draft_number": player.draft_number,
            "image_url": player.image_url,
        }

        team_id = player_data["team_id"]

        team_name = fetch_players_team(team_id)

        player_data["team_name"] = team_name

        return player_data

    return None


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


# Used for testing
if __name__ == "__main__":
    db = SessionLocal()
    try:
        player_id = 2544

        fetch_player_info(db, player_id)
    finally:
        db.close()
