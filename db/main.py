from .db_operations import connect_to_database
from .json_reader import read_json_file
from pathlib import Path

def main():
    current_script_dir = Path(__file__).parent
    json_file_path = current_script_dir / '../data/nba_players.json'
    absolute_json_file_path = json_file_path.resolve()

    players_data = read_json_file(str(absolute_json_file_path))

    if players_data is None:
        return
    conn = connect_to_database()

    if conn is not None:
        cursor = conn.cursor()

        insert_query = '''
        INSERT INTO players (
            person_id, display_last_comma_first, display_first_last, rosterstatus, from_year, 
            to_year, playercode, player_slug, team_id, team_city, team_name, 
            team_abbreviation, team_slug, team_code, games_played_flag, otherleague_experience_ch
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (person_id) DO NOTHING;
        '''

        for player in players_data:
            player_values = (
                player["PERSON_ID"],
                player["DISPLAY_LAST_COMMA_FIRST"],
                player["DISPLAY_FIRST_LAST"],
                player["ROSTERSTATUS"],
                player["FROM_YEAR"],
                player["TO_YEAR"],
                player["PLAYERCODE"],
                player["PLAYER_SLUG"],
                player["TEAM_ID"],
                player["TEAM_CITY"],
                player["TEAM_NAME"],
                player["TEAM_ABBREVIATION"],
                player["TEAM_SLUG"],
                player["TEAM_CODE"],
                player["GAMES_PLAYED_FLAG"],
                player["OTHERLEAGUE_EXPERIENCE_CH"]
            )
            cursor.execute(insert_query, player_values)
        conn.commit()

        cursor.close()
        conn.close()


if __name__ == '__main__':
    main()
