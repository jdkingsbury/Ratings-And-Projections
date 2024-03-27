import sys
from .config import CUSTOM_WEIGHTS
from stats.get_player_stats import get_player_stats, get_max_player_stats, get_min_player_stats


# Normalize the weights
# Make sure the weights add up to 1
# The weights are used to calculate the player's grade
# The player's grade is calculated by multiplying each stat by its weight and summing up the products


# Normalize points per game equation would be: (ppg - min_ppg) / (max_ppg - min_ppg)
# max_ppg = highest ppg in the laeague,
# min_ppg = 0,
# ppg = player's ppg


def normalize_stat(stat, max_stat):
    return stat / max_stat if max_stat else 0


# NOTE: Function to calculate player grade
def calculate_player_grade(player_id, season_id):
    stats = get_player_stats(player_id, season_id)
    player_min_stats = get_min_player_stats(season_id)
    player_max_stats = get_max_player_stats(season_id)

    print(f"Stats: {stats}")
    if not stats or not player_min_stats or not player_max_stats:
        print(f"Error retrieving stats for player {player_id} in season {season_id}")
        return 0

    player_rating = 0


    for stat, weight in CUSTOM_WEIGHTS.items():
        stat_value = stats.get(stat, 0)

        if isinstance(stat_value, (int, float)):
            player_rating += weight * stat_value
        else:
            print(f"Warning: Stat value for {stat} is not a number for player {player_id} in season {season_id}.")

    player_grade = max(0, min(player_rating, 100))
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
