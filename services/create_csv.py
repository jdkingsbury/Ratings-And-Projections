import os
import sys
from .nba_service import (
    get_player_career_stats,
    get_player_id,
    get_all_players,
    get_player_cumulative_stats,
    get_player_game_log,
    get_player_stats
)


def create_csv_file(data, file_name):
    data_directory = "data"
    file_path = os.path.join(data_directory, file_name)

    os.makedirs(data_directory, exist_ok=True)

    with open(file_path, "w") as file:
        file.write(data)


function_mapping = {
    "get_all_players": get_all_players,
    "get_player_career_stats": get_player_career_stats,
    "get_player_id": get_player_id,
    "get_player_cumulative_stats": get_player_cumulative_stats,
    "get_player_game_log": get_player_game_log,
    "get_player_stats": get_player_stats,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python create_csv.py <function> [arguments]")
        sys.exit(1)

    function_name = sys.argv[1]
    args = sys.argv[2:]

    if function_name not in function_mapping:
        print(
            f"Invalid function name. Valid options are: {list(function_mapping.keys())}"
        )
        sys.exit(1)

    if args:
        data = function_mapping[function_name](*args)
        file_name = f"{function_name}_{'_'.join(args)}.csv"
    else:
        data = function_mapping[function_name]()
        file_name = f"{function_name}.csv"

    if data is not None:
        create_csv_file(data, file_name)
        print(f"Data written to {file_name}")


if __name__ == "__main__":
    main()
