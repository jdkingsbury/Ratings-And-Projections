import sys
from .config import CUSTOM_WEIGHTS
from stats.get_player_stats import get_player_stats

# NOTE: Function to calculate player grade
def calculate_player_grade(player_id, season_id):
    stats = get_player_stats(player_id, season_id)

    player_grade = 0

    for stat, weight in CUSTOM_WEIGHTS.items():
        stat_value = stats.get(stat)
        if stat_value is None:
            print(f"Warning: Stat {stat} is missing for player {player_id} in season {season_id}; using 0 instead.")
            stat_value = 0
        player_grade += weight * stat_value
    
    return player_grade

# NOTE: The following code is for testing purposes
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <player_id> <season_id>")
        sys.exit(1)

    player_id_arg = sys.argv[1]
    season_id_arg = sys.argv[2]

    # Convert arguments to appropriate types if necessary
    player_id = int(player_id_arg)
    season_id = season_id_arg  # Assuming season_id is a string like '2023'

    grade = calculate_player_grade(player_id, season_id)
    print(f"Player Grade: {grade}")

