import os

import requests
from bs4 import BeautifulSoup, Tag

# Keeping the code as an example for fetching images.
# May not use team logos since I am unsure if I am legally allowed to.


# Code only fetches the team logo gifs
def fetch_team_logos():
    url = "https://www.sportslogos.net/teams/list_by_league/6/National_Basketball_Association/NBA/logos/"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    logo_wall = soup.find("ul", class_="logoWall")

    if not logo_wall or not isinstance(logo_wall, Tag):
        print("Could not find the logo wall")
        return

    logos = logo_wall.find_all("a")
    os.makedirs("./output/team-logos", exist_ok=True)

    for logo in logos:
        img_tag = logo.find("img")
        if not img_tag:
            continue

        # Extracts the URL of the image from the 'src' attribute
        src = img_tag["src"]

        team_name = logo.get_text(strip=True)

        # Create the url to download the file from
        src_url = f"{src}"

        # Downloads the image using requests module.
        img_response = requests.get(src_url, stream=True)
        img_response.raise_for_status()

        # Save the image to 'team-logos' directory if the request is successful
        # img_name = os.path.basename(team_name)
        img_name = f"{team_name}.gif"
        with open(f"./output/team-logos/{img_name}", "wb") as f:
            for chunk in img_response.iter_content(1024):
                f.write(chunk)
        print(f"Saved {img_name}")


if __name__ == "__main__":
    fetch_team_logos()
