from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class Players(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    is_active = Column(Boolean, index=True)
