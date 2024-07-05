import asyncio
import csv
import json
import os
import sys

from api.routers.nba import (
    get_all_players,
    get_player_career_stats,
    get_player_game_log,
    get_player_info,
)

# TODO: Rewrite Create File
# Look to use the api endpoints to fetch the 
# data rather then trying to call the function

def create_file(data, file_name, output_format):
    data_directory = "../data"
    file_path = os.path.join(data_directory, file_name)

    os.makedirs(data_directory, exist_ok=True)

    if output_format == "json":
        with open(file_path, "w") as file:
            json.dump(json.loads(data), file, indent=4)
    elif output_format == "csv":
        if isinstance(data, str):
            data = json.loads(data)
        keys = data[0].keys() if data else []
        with open(file_path, "w", newline="") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)


# NOTE: Mapping of command-line arguments to functions in nba_service
# Add new functions here when created so that we can create json files for those functions in nba_service.py
function_mapping = {
    "all_players": get_all_players,
    "player_career_stats": get_player_career_stats,
    "player_game_log": get_player_game_log,
    "player_info": get_player_info,
}


async def main():
    if len(sys.argv) < 3:
        print("Usage: python create_file.py <function> <file_name> [arguments]")
        sys.exit(1)

    function_name = sys.argv[1]
    output_format = sys.argv[2]
    args = sys.argv[3:]

    if function_name.startswith("get_"):
        function_name = function_name.replace("get_", "")

    if function_name not in function_mapping:
        print(
            f"Invalid function name. Valid options are: {list(function_mapping.keys())}"
        )
        sys.exit(1)

    if args:
        data = await function_mapping[function_name](*args)
        file_name = f"{function_name}_{'_'.join(args)}.{output_format}"
    else:
        data = await function_mapping[function_name](output_format)
        file_name = f"{function_name}.{output_format}"

    if data is not None:
        create_file(data, file_name, output_format)
        print(f"File created: {file_name}")
    else:
        print(f"No data returned for {function_name} with arguments{args}.")


if __name__ == "__main__":
    asyncio.run(main())
