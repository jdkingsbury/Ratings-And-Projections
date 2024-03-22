from stats.get_player_max_stats import get_max_player_stats

# NOTE: Define weights
CUSTOM_WEIGHTS = {
    'ppg': 0.25,
    'rpg': 0.10,
    'apg': 0.15,
    'spg': 0.10,
    'bpg': 0.10,
    'tov': -0.10,      
    'fg_percent': 0.10,
    'three_point_percent': 0.10,
    'ft_percent': 0.10,
}


