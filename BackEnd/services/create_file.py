import os
import sys

# Determine if running as a script or module
if __name__ == "__main__" and __package__ is None:
    # Set the package to services to allow relative imports
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    __package__ = "services"


from .nba_service import (
    get_all_players,
    get_player_career_stats,
    get_player_cumulative_stats,
    get_player_game_log,
    get_player_id,
    get_player_stats,
)


def create_file(data, file_name):
    data_directory = "data"
    file_path = os.path.join(data_directory, file_name)

    os.makedirs(data_directory, exist_ok=True)

    with open(file_path, "w") as file:
        file.write(data)


# NOTE: Mapping of command-line arguments to functions in nba_service
# Add new functions here when created so that we can create json files for those functions in nba_service.py
function_mapping = {
    "get_all_players": get_all_players,
    "get_player_career_stats": get_player_career_stats,
    "get_player_id": get_player_id,
    "get_player_cumulative_stats": get_player_cumulative_stats,
    "get_player_game_log": get_player_game_log,
    "get_player_stats": get_player_stats,
}


def main():
    if len(sys.argv) < 3:
        print("Usage: python create_file.py <function> <file_name> [arguments]")
        sys.exit(1)

    function_name = sys.argv[1]
    output_format = sys.argv[2]
    args = sys.argv[3:]

    print(f"Function: {function_name}")
    print(f"Output Format: {output_format}")
    print(f"Arguments: {args}")

    if function_name not in function_mapping:
        print(
            f"Invalid function name. Valid options are: {list(function_mapping.keys())}"
        )
        sys.exit(1)

    if args:
        data = function_mapping[function_name](*args, output_format)
        function_name = function_name.replace("get_", "")
        file_name = f"{function_name}_{'_'.join(args)}.{output_format}"
    else:
        data = function_mapping[function_name](output_format)
        function_name = function_name.replace("get_", "")
        file_name = f"{function_name}.{output_format}"

    print(f"Constructed file name: {file_name}")

    if data is not None:
        create_file(data, file_name)
        print(f"File created: {file_name}")
    else:
        print(f"No data returned for {function_name} with arguments{args}.")


if __name__ == "__main__":
    main()
