export interface PlayerInfo {
  PERSON_ID: number;
  FIRST_NAME: string;
  LAST_NAME: string;
  DISPLAY_FIRST_LAST: string;
  DISPLAY_LAST_COMMA_FIRST: string;
  DISPLAY_FI_LAST: string;
  PLAYER_SLUG: string;
  BIRTHDATE: string;
  SCHOOL: string;
  COUNTRY: string;
  LAST_AFFILIATION: string;
  HEIGHT: string;
  WEIGHT: string;
  SEASON_EXP: number;
  JERSEY: string;
  POSITION: string;
  ROSTERSTATUS: string;
  GAMES_PLAYED_CURRENT_SEASON_FLAG: string;
  TEAM_ID: number;
  TEAM_NAME: string;
  TEAM_ABBREVIATION: string;
  TEAM_CODE: string;
  TEAM_CITY: string;
  PLAYERCODE: string;
  FROM_YEAR: number;
  TO_YEAR: number;
  DLEAGUE_FLAG: string;
  NBA_FLAG: string;
  GAMES_PLAYED_FLAG: string;
  DRAFT_YEAR: string;
  DRAFT_ROUND: string;
  DRAFT_NUMBER: string;
  GREATEST_75_FLAG: string;
  IMAGE_URL: string;
}

export interface CareerStats {
  PERSON_ID: number;
  SEASON_ID: string;
  LEAGUE_ID: string;
  TEAM_ID: number;
  TEAM_ABBREVIATION: string;
  PLAYER_AGE: number;
  GP: number;
  GS: number;
  MIN: number;
  FGM: number;
  FGA: number;
  FG_PCT: number;
  FG3M: number;
  FG3A: number;
  FG3_PCT: number;
  FTM: number;
  FTA: number;
  FT_PCT: number;
  OREB: number;
  DREB: number;
  REB: number;
  AST: number;
  STL: number;
  BLK: number;
  TOV: number;
  PF: number;
  PTS: number;
}

export interface PlayerGameLog {

}
