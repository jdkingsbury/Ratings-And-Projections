from app.db.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# League ID:
# - NBA: 01

class Player(Base):
    __tablename__ = "players"

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
    team_id = Column(Integer, ForeignKey("teams.id"))
    from_year = Column(Integer)
    to_year = Column(Integer)
    draft_year = Column(String(25))
    draft_round = Column(String(25))
    draft_number = Column(String(25))
    image_url = Column(String(255))

    team = relationship("Team", back_populates="players")

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.position}"


class Sport(Base):
    __tablename__ = "sports"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    leagues = relationship("League", back_populates="sport")


class League(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    sport_id = Column(Integer, ForeignKey("sports.id"))

    sport = relationship("Sport", back_populates="leagues")
    teams = relationship("Team", back_populates="league")


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100))
    abbreviation = Column(String(5))
    nickname = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    league_id = Column(Integer, ForeignKey("leagues.id"))

    players = relationship("Player", back_populates="team")
    league = relationship("League", back_populates="teams")
