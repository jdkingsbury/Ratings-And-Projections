import argparse
from datetime import datetime
from typing import Any

import pandas as pd
import requests

# New version of create_file using pandas and argparse to simplify the code

def fetch_data_from_api(endpoint_url: str) -> Any:
    response = requests.get(endpoint_url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def save_data_to_json(data: Any, filename: str) -> None:
    df = pd.json_normalize(data)
    df.to_json(f"/app/output/{filename}", orient="records", lines=True)


def save_data_to_csv(data: Any, filename: str) -> None:
    df = pd.json_normalize(data)
    df.to_csv(f"/app/output/{filename}", index=False)


def generate_filename(base_name: str, extension: str) -> str:
    # Might add current time but will need to find a nice format
    # current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}.{extension}"

def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch data from an API and save it as a JSON or CSV.")
    parser.add_argument("api_url",type=str, help="The URL of the API to fetch data from.")
    parser.add_argument("file_type",type=str, choices=["json", "csv"], help="The type of file to save the data as (json or csv).")
    parser.add_argument("base_name",type=str, help="The base name for the saved file.")

    args = parser.parse_args()

    data = fetch_data_from_api(args.api_url)

    if args.file_type == 'json':
        filename = generate_filename(args.base_name, "json")
        save_data_to_json(data, filename)
        print(f"Data saved to /app/output/{filename}")
    elif args.file_type == 'csv':
        filename = generate_filename(args.base_name, "csv")
        save_data_to_csv(data, filename)
        print(f"Data saved to /app/output/{filename}")
    else:
        print("Invalid file type. Please enter either 'json' or 'csv'.")

if __name__ == "__main__":
    main()
