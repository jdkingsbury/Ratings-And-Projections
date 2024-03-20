# Description: Helper functions for stats module

# NOTE: Helper function to calculate per game stats
def calculate_per_game_stat(total_stat, games_played, precision=1):
    return round(total_stat / games_played, precision) if games_played else 0


# NOTE: Helper function to calculate percentage stats
def calculate_percentage_stat(made, attempted, precision=1):
    return round((made / attempted) * 100, precision) if attempted else 0.0


def validate_stat_data(data, stat_name):
    if not isinstance(data, (tuple, list)) or len(data) != 2:
        raise ValueError(f"{stat_name} data is invalid or does not contain expected elements")
    
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError(f"Elements in {stat_name} data are not of type int or float")

    return data


