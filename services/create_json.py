import os
import sys
import json
from .nba_service import get_player_career_stats, get_player_id, get_all_players

def create_json_file(data, file_name):
    data_directory = 'data'
    file_path = os.path.join(data_directory, file_name)

    os.makedirs(data_directory, exist_ok=True)

    with open(file_path, 'w') as file:
        file.write(data)

# Mapping of command-line arguments to functions in nba_service
function_mapping = {
    'get_all_players': get_all_players,
    'get_player_career_stats': get_player_career_stats,
    'get_player_id': get_player_id
}

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_json.py <function> [arguments]")
        sys.exit(1)

    function_name, arg = sys.argv[1], sys.argv[2]

    if function_name not in function_mapping:
        print(f"Invalid function name. Valid options are: {list(function_mapping.keys())}")
        sys.exit(1)

    data = function_mapping[function_name](arg)

    if data is not None:
        create_json_file(data, f"{function_name}_{arg}.json")
        print(f"Data written to {function_name}_{arg}.json")

if __name__ == '__main__':
    main()

