from .nba_service import get_player_id, get_player_career_stats

# NOTE: Will create json files here possibly or have a separate files to do it
# with open('player.json', 'w') as file:
#     json.dump(get_player_career_stats(1630173), file)

def main():
    print(get_player_id('LeBron James'))
    print(get_player_career_stats(2544))

if __name__ == '__main__':
    main()
