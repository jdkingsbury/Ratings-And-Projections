from typing import List, Optional

import sqlalchemy as sa
from app.db.database import SessionLocal
from app.utils.nba_utils import fetch_players_team

# Players


def fetch_player_card_info(db, player_id: int) -> Optional[dict]:
    """Fetches NBA Player Card Info"""
    query = sa.text(
        """
        SELECT player_id, first_last, team_id
        FROM nba_players
        WHERE player_id = :player_id
    """
    )

    result = db.execute(query, {"player_id": player_id}).fetchone()

    if result:
        card_data = {
            "player_id": result[0],
            "first_last": result[1],
            "team_id": result[2],
        }

        team_id = card_data["team_id"]
        team_name = fetch_players_team(team_id)

        card_data["team_name"] = team_name
        del card_data["team_id"]

        return card_data

    return None


def fetch_players(db) -> List[dict]:
    """Fetches all NBA Players from the database."""
    query = sa.text("SELECT * FROM nba_players")
    players = db.execute(query).fetchall()

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
        }

        team_id = player_data["team_id"]
        team_name = fetch_players_team(team_id) if team_id else None
        player_data["team_name"] = team_name

        players_with_team_names.append(player_data)

    return players_with_team_names


def fetch_player_info(db, player_id: int) -> Optional[dict]:
    """Fetches information of a specific NBA player by player_id."""
    query = sa.text(
        """
        SELECT * 
        FROM nba_players
        WHERE player_id = :player_id
    """
    )

    result = db.execute(query, {"player_id": player_id}).fetchone()

    if result:
        player_data = {
            "player_id": result.player_id,
            "first_last": result.first_last,
            "first_name": result.first_name,
            "last_name": result.last_name,
            "birth_date": result.birth_date,
            "school": result.school,
            "country": result.country,
            "height": result.height,
            "weight": result.weight,
            "jersey": result.jersey,
            "position": result.position,
            "is_active": result.is_active,
            "team_id": result.team_id,
            "from_year": result.from_year,
            "to_year": result.to_year,
            "draft_year": result.draft_year,
            "draft_round": result.draft_round,
            "draft_number": result.draft_number,
        }

        team_id = player_data["team_id"]
        team_name = fetch_players_team(team_id)

        player_data["team_name"] = team_name

        return player_data

    return None


def fetch_last_five_games_for_player(db, player_id: int, season_year: str):
    """Fetches the last 5 games for a specific NBA player."""
    query = sa.text(
        """
        SELECT *
        FROM nba_game_logs
        WHERE player_id = :player_id
        AND season_year = :season_year
        ORDER BY game_date DESC
        LIMIT 5
    """
    )
    return db.execute(
        query, {"player_id": player_id, "season_year": season_year}
    ).fetchall()


# Teams


def fetch_teams(db) -> List[dict]:
    """Fetches all NBA Teams from the database"""
    query = sa.text("SELECT * FROM nba_teams")
    return db.execute(query).fetchall()


def fetch_team_info(db, team_id: int) -> Optional[dict]:
    """Fetches information of a specific NBA team by team_id"""
    query = sa.text(
        """
        SELECT *
        FROM nba_teams
        WHERE team_id = :team_id
        """
    )

    result = db.execute(query, {"team_id": team_id}).fetchone()

    if result:
        team_data = {
            "team_id": result.team_id,
            "name": result.name,
            "abbreviation": result.abbreviation,
            "nickname": result.nickname,
            "city": result.city,
            "state": result.state,
            "conference": result.conference,
            "division": result.division,
            "year_founded": result.year_founded,
            "w": result.w,
            "l": result.l,
            "pct": result.pct,
            "conf_rank": result.conf_rank,
            "div_rank": result.div_rank,
            "season_year": result.season_year,
            "league_id": result.league_id,
        }

        return team_data

    return None


# Used for testing
if __name__ == "__main__":
    db = SessionLocal()
    try:
        player_id = 2544
        fetch_player_info(db, player_id)
    finally:
        db.close()
