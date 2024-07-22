from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(50))
    first_name = Column(String(25))
    last_name = Column(String(25))
    birth_date = Column(String(15))
    position = Column(String(15))
    is_active = Column(Boolean)
    team_id = Column(Integer, ForeignKey("teams.id"))

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


