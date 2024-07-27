from app.db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Sport(Base):
    __tablename__ = "sports"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    leagues = relationship("League", back_populates="sport", cascade="all, delete-orphan")


