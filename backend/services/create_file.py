import asyncio
import json
import os
import sys

import httpx
import pandas as pd

BASE_URL = "http://127.0.0.1:8000"

# TODO: Redoing file 

def create_file(data, file_name, output_format):
    data_dir = "../data"
    file_path = os.path.join(data_dir, file_name)

    os.makedirs(data_dir, exist_ok=True)

    if output_format == "json":
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    elif output_format == "csv":
        with open(file_path, "w") as file:
            df = pd.DataFrame(data)
            df.to_csv(file, index=False)


async def fetch_data(endpoint, params):
    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()


async def main():
    if len(sys.argv) < 4:
        print(
            "Usage: python create_file.py <sports_league> <type_of_data> <output_format> <args...>"
        )
        sys.exit(1)

    sports_league = sys.argv[1]
    type_of_data = sys.argv[2]
    output_format = sys.argv[3]
    args = sys.argv[4:]

    endpoint = f"{BASE_URL}/{sports_league}/{type_of_data}/{'/'.join(args)}"
    params = {"output_format": output_format}

    try:
        data = await fetch_data(endpoint, params)
        file_name = f"{type_of_data}_{sports_league}_{'_'.join(args)}.{output_format}"

        if data is not None:
            create_file(data, file_name, output_format)
            print(f"File created: {file_name}")
        else:
            print(f"No data returned for {type_of_data} with arguments {args}.")
    except httpx.HTTPStatusError as e:
        print(f"HTTP Exception: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())
