from db_operations import connect_to_database
from json_reader import read_json_file

def main():
    players_data = read_json_file('players.json')
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
            cursor.execute(insert_query, player)

        conn.commit()

        cursor.close()
        conn.close()


if __name__ == '__main__':
    main()
