from app.db.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class League(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    sport_id = Column(Integer, ForeignKey("sports.id"))

    sport = relationship("Sport", back_populates="leagues")
    teams = relationship("NBATeam", back_populates="league", cascade="all, delete-orphan")
