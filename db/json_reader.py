import json

# NOTE: This function reads a JSON file and returns the data.
def read_json_file(file_path):
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
