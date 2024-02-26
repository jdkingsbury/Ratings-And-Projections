#NOTE: Might not need math
import math
import numpy as np

# Might not need any of these functions
def Calculate_Steal_Percentage(steals, team_minutes_played, minutes_played, opponents_possessions):
    stealpercentage = 100 * (steals * (team_minutes_played / 5)) / (minutes_played * opponents_possessions)
    return stealpercentage

def Calculate_Block_Percentage(blocks, team_minutes_played, minutes_played, opponents_field_goals_attempted, opponents_three_point_field_goals_attempted):
    blockpercentage = 100 * (blocks * (team_minutes_played / 5)) / (minutes_played * (opponents_field_goals_attempted - opponents_three_point_field_goals_attempted))
    return blockpercentage

def Calculate_Defensive_Rebound_Percentage(defensive_rebounds, team_minutes_played, minutes_played, team_offensive_rebounds, opponents_defensive_rebounds):
    defensivereboundpercentage = 100 * (defensive_rebounds * (team_minutes_played / 5)) / (minutes_played * (team_offensive_rebounds + opponents_defensive_rebounds))
    return defensivereboundpercentage

# Need to read the book Dean Oliver's book Basketball on Paper to get correct calculation
def Calculate_Defensive_Rating(opponents_points, team_defensive_possessions):
    defensiverating = 100 * opponents_points / team_defensive_possessions
    return defensiverating

def Calculate_Defensive_Win_Shares(minutes_played, team_minutes_played, team_defensive_possession, league_points_per_possession, defensive_rating, league_points_per_game, team_pace, league_pace):
    defensivewinshares = ((minutes_played/team_minutes_played)*team_defensive_possession)*(((1.08*league_points_per_possession)-(defensive_rating/100))/((0.32*league_points_per_game)*(team_pace/league_pace)))
    return defensivewinshares
