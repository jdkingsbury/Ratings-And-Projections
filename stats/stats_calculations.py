# Description: This file contains functions that are used to calculate stats for players.


# NOTE: Function to calculate points per game
def calculate_ppg(data):
    games_played = data.games_played
    total_points = data.total_points

    if games_played > 0:
        return total_points / games_played
    return 0


# NOTE: Mapping of calculation functions
calculation_function_mapping = {
    "calculate_ppg": calculate_ppg,
}
