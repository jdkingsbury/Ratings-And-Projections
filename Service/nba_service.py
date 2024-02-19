import nba_api.stats.endpoints as playercareerstats

# Anthony Davis
career = playercareerstats.PlayerCareerStats(player_id="203076")
career.get_data_frames()[0]

print(career.get_data_frames()[0].head(1))

