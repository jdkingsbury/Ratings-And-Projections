from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Player(Base):
    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True)
    first_last = Column(String(50))
    first_name = Column(String(30))
    last_name = Column(String(30))
    birth_date = Column(String(30))
    school = Column(String(50))
    country = Column(String(30))
    height = Column(Integer)
    weight = Column(Integer)
    jersey = Column(Integer)
    position = Column(String(30))
    is_active = Column(Boolean)
    team_id = Column(Integer, ForeignKey("teams.id"))
    from_year = Column(Integer)
    to_year = Column(Integer)
    draft_year = Column(Integer)
    draft_round = Column(Integer)
    draft_number = Column(Integer)
    image_url = Column(String(255))

    team = relationship("Team", back_populates="players")

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.position}"


class Sport(Base):
    __tablename__ = "sports"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    leagues = relationship("League", back_populates="sport")


class League(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    sport_id = Column(Integer, ForeignKey("sports.id"))

    sport = relationship("Sport", back_populates="leagues")
    teams = relationship("Team", back_populates="league")


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(50))
    abbreviation = Column(String(3))
    nickname = Column(String(20))
    city = Column(String(20))
    state = Column(String(20))
    league_id = Column(Integer, ForeignKey("leagues.id"))

    team = relationship("League", back_populates="teams")
    players = relationship("Player", back_populates="team")
