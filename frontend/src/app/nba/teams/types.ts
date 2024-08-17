export type Team = {
  team_id: number;
  name: string;
  abbreviation: string;
  nickname: string;
  city: string;
  state: string;
  conference: string;
  division: string;
  year_founded: string;
  w: string;
  l: string;
  pct: number;
  conf_rank: number;
  div_rank: number;
  season_year: string;
  league_id: number;
};

export type Division = {
  divisionName: string;
  teams: Team[];
};
