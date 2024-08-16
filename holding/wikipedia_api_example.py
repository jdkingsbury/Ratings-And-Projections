import requests

# Example of using Wikipedia API
base_url = "https://en.wikipedia.org/w/api.php"


def fetch_team_info():
    params = {
        "action": "query",
        "prop": "pageimages",
        "titles": "Atlanta Hawks",
        "format": "json",
        "pithumbsize": 500,
    }

    response = requests.get(base_url, params=params)

    if not response.ok:
        print("Failed to fetch team data from wiki api")
        return None

    data = response.json()

    print(data)


if __name__ == "__main__":
    fetch_team_info()
