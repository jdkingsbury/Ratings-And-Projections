# Description: This file contains functions that are used to calculate stats for players.

from stats.helper_functions import (calculate_per_game_stat, calculate_percentage_stat, validate_stat_data,)


# NOTE: Function to calculate points per game
def calculate_ppg(data):
    if len(data) == 2:
        total_points, games_played = validate_stat_data(data, "PPG")
        return calculate_per_game_stat(total_points, games_played)
    return 0


# NOTE: Function to calculate rebounds per game
def calculate_rpg(data):
    if len(data) == 2:
        total_rebounds, games_played = validate_stat_data(data, "RPG")
        return calculate_per_game_stat(total_rebounds, games_played)


# NOTE: Function to calculate assists per game
def calculate_apg(data):
    if len(data) == 2:
        total_assists, games_played = validate_stat_data(data, "APG")
        return calculate_per_game_stat(total_assists, games_played)


# NOTE: Function to calculate steals per game
def calculate_spg(data):
    if len(data) == 2:
        total_steals, games_played = validate_stat_data(data, "SPG")
        return calculate_per_game_stat(total_steals, games_played)


# NOTE: Function to calculate blocks per game
def calculate_bpg(data):
    if len(data) == 2:
        total_blocks, games_played = validate_stat_data(data, "BPG")
        return calculate_per_game_stat(total_blocks, games_played)


# NOTE: Function to calculate turnovers per game
def calculate_tov(data):
    if len(data) == 2:
        total_turnovers, games_played = validate_stat_data(data, "TOV")
        return calculate_per_game_stat(total_turnovers, games_played)

def calculate_fg_percent(data):
    fg_pct = validate_stat_data(data, "FG%")
    return fg_pct

def calculate_three_point_percent(data):
    three_point_pct = validate_stat_data(data, "3P%")
    return three_point_pct

def calculate_ft_percent(data):
    ft_percent = validate_stat_data(data, "FT%")
    return ft_percent


# NOTE: Mapping of calculation functions
calculation_function_mapping = {
    "ppg": calculate_ppg,
    "rpg": calculate_rpg,
    "apg": calculate_apg,
    "spg": calculate_spg,
    "bpg": calculate_bpg,
    "tov": calculate_tov,
    "fg_percent": calculate_fg_percent,
    "three_point_percent": calculate_three_point_percent,
    "ft_percent": calculate_ft_percent,
}
