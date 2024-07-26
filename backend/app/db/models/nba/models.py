from app.db.database import Base
from app.db.models.sports.models import Team
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


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
