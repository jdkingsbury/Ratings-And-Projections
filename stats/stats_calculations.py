# Description: This file contains functions that are used to calculate stats for players.


# NOTE: Function to calculate points per game
def calculate_ppg(data):
    if len(data) == 2:
        total_points, games_played = data
        return total_points / games_played if games_played else 0
    else:
        raise ValueError("Data does not contain expected elements")


# NOTE: Function to calculate rebounds per game
def calculate_rpg(data):
    if len(data) == 2:
        total_rebounds, games_played = data
        return total_rebounds / games_played if games_played else 0
    else:
        raise ValueError("Data does not contain expected elements")


# NOTE: Function to calculate assists per game
def calculate_apg(data):
    if len(data) == 2:
        total_assists, games_played = data
        return total_assists / games_played if games_played else 0
    else:
        raise ValueError("Data does not contain expected elements")

# NOTE: Function to calculate steals per game
def calculate_spg(data):
    if len(data) == 2:
        total_steals, games_played = data
        return total_steals / games_played if games_played else 0
    else:
        raise ValueError("Data does not contain expected elements")

# NOTE: Function to calculate blocks per game
def calculate_bpg(data):
    if len(data) == 2:
        total_blocks, games_played = data
        return total_blocks / games_played if games_played else 0
    else:
        raise ValueError("Data does not contain expected elements")

# NOTE: Function to calculate turnovers per game
def calculate_tov(data):
    if len(data) == 2:
        total_turnovers, games_played = data
        return total_turnovers / games_played if games_played else 0
    else:
        raise ValueError("Data does not contain expected elements")

# NOTE: Function to calculate field goal percentage
def calculate_fg_percent(data):
    if len(data) == 2:
        field_goals_made, field_goals_attempted = data
        return field_goals_made / field_goals_attempted if field_goals_attempted else 0
    else:
        raise ValueError("Data does not contain expected elements")

# NOTE: Function to calculate three point percentage
def calculate_three_point_percent(data):
    if len(data) == 2:
        three_pointers_made, three_pointers_attempted = data
        return three_pointers_made / three_pointers_attempted if three_pointers_attempted else 0
    else:
        raise ValueError("Data does not contain expected elements")

# NOTE: Mapping of calculation functions
calculation_function_mapping = {
    "ppg": calculate_ppg,
}
