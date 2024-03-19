# Description: This file contains functions that are used to calculate stats for players.


# NOTE: Function to calculate points per game
def calculate_ppg(data):
    if len(data) == 2:
        total_points, games_played = data
        return total_points / games_played if games_played else 0
    else:
        raise ValueError("Data does not contain expected elements")



# NOTE: Mapping of calculation functions
calculation_function_mapping = {
    "ppg": calculate_ppg,
}
