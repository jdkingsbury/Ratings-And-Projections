import sys
from .config import CUSTOM_WEIGHTS
from stats.get_player_stats import get_player_stats

# NOTE: Function to calculate player grade
def calculate_player_grade(player_id, season_id):
    stats = get_player_stats(player_id, season_id)

    player_grade = 0

    for stat, weight in CUSTOM_WEIGHTS.items():
        stat_value = stats.get(stat, 0)  # Ensure a default value of 0 if the stat is missing

        # Check if stat_value is None and replace it with 0
        if stat_value is None:
            stat_value = 0

        # Ensure stat_value is a number before multiplication
        if isinstance(stat_value, (int, float)):
            player_grade += weight * stat_value
        else:
            print(f"Warning: Stat value for {stat} is not a number for player {player_id} in season {season_id}.")
    
    # Ensure the grade is between 0 and 100
    player_grade = max(0, min(player_grade, 100))
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

