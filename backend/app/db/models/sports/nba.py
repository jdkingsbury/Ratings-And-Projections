from app.db.database import Base
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class NBAPlayer(Base):
    __tablename__ = "nba_players"

    player_id = Column(Integer, primary_key=True)
    first_last = Column(String(100))
    first_name = Column(String(50))
    last_name = Column(String(50))
    birth_date = Column(Date)
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
    draft_year = Column(String(25), nullable=True)
    draft_round = Column(String(25), nullable=True)
    draft_number = Column(String(25), nullable=True)
    image_url = Column(String(255))

    nba_team = relationship("NBATeam", back_populates="nba_players")
    game_logs = relationship("NBAGameLog", back_populates="player")


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


class NBAGameLog(Base):
    __tablename__ = "nba_game_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    season_id = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey("nba_players.player_id"))
    game_id = Column(String, nullable=False)
    game_date = Column(Date, nullable=False)
    matchup = Column(String(100), nullable=False)
    wl = Column(String(5), nullable=True)
    min = Column(Integer, nullable=True)
    fgm = Column(Integer, nullable=True)
    fga = Column(Integer, nullable=True)
    fg_pct = Column(Float, nullable=True)
    fg3m = Column(Integer, nullable=True)
    fg3a = Column(Integer, nullable=True)
    fg3_pct = Column(Float, nullable=True)
    ftm = Column(Integer, nullable=True)
    fta = Column(Integer, nullable=True)
    ft_pct = Column(Float, nullable=True)
    oreb = Column(Integer, nullable=True)
    dreb = Column(Integer, nullable=True)
    reb = Column(Integer, nullable=True)
    ast = Column(Integer, nullable=True)
    stl = Column(Integer, nullable=True)
    blk = Column(Integer, nullable=True)
    tov = Column(Integer, nullable=True)
    pf = Column(Integer, nullable=True)
    pts = Column(Integer, nullable=True)
    plus_minus = Column(Float, nullable=True)
    video_available = Column(Boolean, nullable=True)
    season_year = Column(String, nullable=False)

    player = relationship("NBAPlayer", back_populates="game_logs")
