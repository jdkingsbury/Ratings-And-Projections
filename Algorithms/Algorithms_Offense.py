# NOTE: Might not need math
import math
import numpy as np

# TODO: Rewrite all the reamining functions
def Calculate_Assist_Percentage(assist, minutes_played, team_minutes_played, team_field_goals, field_goals):
    assistpercentage = 100 * assist / (((minutes_played / (team_minutes_played / 5)) * team_field_goals) - field_goals)
    return assistpercentage

def Calculate_Turnover_Percentage(turnover, field_goals_attempted, free_throws_attempted, turnovers):
    turnoverpercentage = 100 * turnover / (field_goals_attempted + 0.44 * free_throws_attempted + turnovers)
    return turnoverpercentage

def Calculate_Offensive_Rebound_Percentage(offensive_rebounds, team_minutes_played, minutes_played, team_offensive_rebounds, opponents_defensive_rebounds):
    offensivereboundpercentage = 100 * (offensive_rebounds * (team_minutes_played / 5)) / (minutes_played * (team_offensive_rebounds + opponents_defensive_rebounds))
    return offensivereboundpercentage

def Calculate_Effective_Field_Goal_Percentage(field_goals, three_point_field_goals, field_goals_attempted):
    effectivefieldgoalpercentage = (field_goals + 0.5 * three_point_field_goals) / field_goals_attempted
    return effectivefieldgoalpercentage

def Calculate_True_Shooting_Percentage(points, field_goals_attempted, free_throws_attempted):
    trueshootingpercentage = points / (2 * (field_goals_attempted + 0.44 * free_throws_attempted))
    return trueshootingpercentage

def Calculate_Usage_Rate(field_goals_attempted, free_throws_attempted, turnovers, team_minutes_played, minutes_played, team_field_goals_attempted, team_free_throws_attempted, team_turnovers):
    usgrate = 100 * ((field_goals_attempted + 0.44 * free_throws_attempted + turnovers) * (team_minutes_played / 5)) / (minutes_played * (team_field_goals_attempted + 0.44 * team_free_throws_attempted + team_turnovers))
    return usgrate

def Calculate_Points_Per_Possession(points, field_goals_attempted, free_throws_attempted, turnovers):
    pointsperpossession = points / (field_goals_attempted + 0.44 * free_throws_attempted + turnovers)
    return pointsperpossession

def Calculate_Offensive_Rating(points, field_goals_attempted, free_throws_attempted, turnovers, team_possessions):
    offensiverating = 100 * (points / (field_goals_attempted + 0.44 * free_throws_attempted + turnovers)) / team_possessions
    return offensiverating

def Calculate_Offensive_Win_Shares(points, league_points_per_possession, field_goals_attempted, free_throws_attempted, turnovers, league_points_per_game, team_pace, league_pace):
    offensivewinshares = (points - 0.92 * league_points_per_possession * (field_goals_attempted + 0.44 * free_throws_attempted + turnovers)) / (0.32 * league_points_per_game * (team_pace / league_pace))
    return offensivewinshares


