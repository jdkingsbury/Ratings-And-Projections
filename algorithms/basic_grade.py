from .config import CUSTOM_WEIGHTS
from db.retrieve_data import retrieve_and_calculate_data

def calculate_player_grade(player_id, season_id, weights):

    ppg = retrieve_and_calculate_data('get_total_points_and_games_played', 'ppg', player_id, season_id)
    rpg = retrieve_and_calculate_data('get_total_rebounds_and_games_played', 'rpg', player_id, season_id)

    player_grade = (weights['ppg'] * ppg) + (weights['rpg'] * rpg) + (weights['apg'] * apg) + \
                   (weights['spg'] * spg) + (weights['bpg'] * bpg) - (weights['tov'] * tov) + \
                   (weights['fg_percent'] * fg_percent) + (weights['three_point_percent'] * three_point_percent) + \
                   (weights['ft_percent'] * ft_percent)
    
    return player_grade


# NOTE: Example player stats
ppg = 25
rpg = 10
apg = 5
spg = 1.5
bpg = 1
tov = 3
fg_percent = 50
three_point_percent = 35
ft_percent = 85

# NOTE: Calculate the player's grade with custom weights
player_grade = calculate_player_grade(ppg, rpg, apg, spg, bpg, tov, fg_percent, three_point_percent, ft_percent, CUSTOM_WEIGHTS)

print(f"Player Grade: {player_grade}")


