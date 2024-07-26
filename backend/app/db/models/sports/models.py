from app.db.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

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
