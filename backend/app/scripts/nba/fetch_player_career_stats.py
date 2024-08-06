import pandas as pd
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players


# Reference fetch_teams on an example of replacing league_id
def fetch_player_career_stats(player_id: int):
    player_career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    player_career_stats_df = player_career_stats.get_data_frames()[0]

    if player_career_stats_df.empty:
        return pd.DataFrame()

    player_career_stats_df = player_career_stats_df.rename(
        columns={
            "PLAYER_ID": "player_id",
            "SEASON_ID": "season_id",
            # NOTE: League_id column will need to be changed to use ours
            "LEAGUE_ID": "league_id",
            "TEAM_ID": "team_id",
            "TEAM_ABBREVIATION": "team_abbreviation",
            "PLAYER_AGE": "player_age",
            "GP": "gp",
            "GS": "gs",
            "MIN": "min",
            "FGM": "fgm",
            "FGA": "fga",
            "FG_PCT": "fg_pct",
            "FG3M": "fg3m",
            "FG3A": "fg3a",
            "FG3_PCT": "fg3_pct",
            "FTM": "ftm",
            "FTA": "fta",
            "FT_PCT": "ft_pct",
            "OREB": "oreb",
            "DREB": "dreb",
            "REB": "reb",
            "AST": "ast",
            "STL": "stl",
            "BLK": "blk",
            "TOV": "tov",
            "PF": "pf",
            "PTS": "pts",
        }
    )


#
def get_all_player_ids() -> list[int]:
    all_players = players.get_players()
    active_players = [player for player in all_players if player["is_active"]]
    player_ids = [player["id"] for player in active_players]
    return player_ids


def main():
    print(fetch_player_career_stats(2544))


if __name__ == "__main__":
    main()
