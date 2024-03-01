import json

def load_players_data(file_path):
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
        return json_data
    except FileNotFoundError:
        print('File not found.')
        exit(1)
    except json.JSONDecodeError:
        print('JSON decoding failed.')
        exit(1)
