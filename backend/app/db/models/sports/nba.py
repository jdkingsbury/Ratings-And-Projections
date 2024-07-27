from app.db.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from app.db.models.league import League
from sqlalchemy.orm import relationship


class NBAPlayer(Base):
    __tablename__ = "nba_players"

    player_id = Column(Integer, primary_key=True)
    first_last = Column(String(100))
    first_name = Column(String(50))
    last_name = Column(String(50))
    birth_date = Column(String(50))
    school = Column(String(100))
    country = Column(String(100))
    height = Column(String(10))
    weight = Column(String(10))
    jersey = Column(String(10))
    position = Column(String(50))
    is_active = Column(Boolean)
    from_year = Column(Integer)
    to_year = Column(Integer)
    team_id = Column(Integer, ForeignKey("nba_teams.id"))
    draft_year = Column(String(25))
    draft_round = Column(String(25))
    draft_number = Column(String(25))
    image_url = Column(String(255))

    nba_team = relationship("NBATeam", back_populates="nba_players")

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.position}"


# Change to NBA teams
class NBATeam(Base):
    __tablename__ = "nba_teams"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100))
    abbreviation = Column(String(5))
    nickname = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    country = Column(String(50))
    league_id = Column(Integer, ForeignKey("leagues.id"))

    league = relationship("League", back_populates="teams")
    nba_players = relationship(
        "NBAPlayer", back_populates="nba_team", cascade="all, delete-orphan"
    )
