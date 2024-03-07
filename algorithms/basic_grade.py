
def calculate_player_grade(ppg, rpg, apg, spg, bpg, tov, fg_percent, three_point_percent, ft_percent, weights):
    player_grade = (weights['ppg'] * ppg) + (weights['rpg'] * rpg) + (weights['apg'] * apg) + \
                   (weights['spg'] * spg) + (weights['bpg'] * bpg) - (weights['tov'] * tov) + \
                   (weights['fg_percent'] * fg_percent) + (weights['three_point_percent'] * three_point_percent) + \
                   (weights['ft_percent'] * ft_percent)
    
    return player_grade

# Define weights
custom_weights = {
    'ppg': 4, 'rpg': 2, 'apg': 3, 'spg': 1.5, 'bpg': 1.5, 
    'tov': -2, 'fg_percent': 1, 'three_point_percent': 1, 'ft_percent': 1
}

# Example player stats
ppg = 25
rpg = 10
apg = 5
spg = 1.5
bpg = 1
tov = 3
fg_percent = 50
three_point_percent = 35
ft_percent = 85

# Calculate the player's grade with custom weights
player_grade = calculate_player_grade(ppg, rpg, apg, spg, bpg, tov, fg_percent, three_point_percent, ft_percent, custom_weights)

print(f"Player Grade: {player_grade}")


