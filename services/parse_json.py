import json

def parse_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
