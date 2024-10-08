from datetime import date
from typing import Optional

from pydantic import BaseModel


class NBAPlayerBase(BaseModel):
    player_id: int
    first_last: str
    first_name: str
    last_name: str
    birth_date: Optional[date]
    school: Optional[str]
    country: Optional[str]
    height: Optional[str]
    weight: Optional[str]
    jersey: Optional[str]
    position: Optional[str]
    is_active: bool
    team_id: Optional[int]
    team_name: Optional[str]
    from_year: Optional[int]
    to_year: Optional[int]
    draft_year: Optional[str] = None
    draft_round: Optional[str] = None
    draft_number: Optional[str] = None

    class Config:
        from_attributes = True


# For Testing Recent Games
class NBAGameLogBase(BaseModel):
    game_date: date
    matchup: str
    wl: Optional[str]
    min: Optional[int]
    fgm: Optional[int]
    fga: Optional[int]
    fg_pct: Optional[float]
    fg3m: Optional[int]
    fg3a: Optional[int]
    fg3_pct: Optional[float]
    ftm: Optional[int]
    fta: Optional[int]
    ft_pct: Optional[float]
    reb: Optional[int]
    ast: Optional[int]
    stl: Optional[int]
    blk: Optional[int]
    tov: Optional[int]
    pf: Optional[int]
    pts: Optional[int]

    class Config:
        from_attributes = True


class NBATeamBase(BaseModel):
    team_id: int
    name: str
    abbreviation: str
    nickname: str
    city: str
    state: str
    conference: str
    division: str
    year_founded: str
    w: str
    l: str
    pct: float
    conf_rank: int
    div_rank: int
    season_year: str
    league_id: int

    class Config:
        from_attributes = True


class NBAPlayerCardInfo(BaseModel):
    player_id: int
    first_last: str
    team_name: str

    class Config:
        from_attributes = True
