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

def OffRebPerc():
    100 * (ORB * (TMP / 5) / (MP * (TORB + ODRB))
    # ORB=Offensive Rebounds
    # TMP=Team Minutes Played
    # MP=Minutes Played
    # TORB=Team Offensive Rebounds
    # ODRB=Opponents Defensive Rebounds

def eFGPerc():
    (FG + 0.5 * 3P) / FGA
    # FG = Field Goals
    # 3P = Three Pointers
    # FGA = Field Goal Attempts

def TrueShootingPerc():
    PT / (2 * (FGA + 0.44 * FTA))
    # PT = Points
    # FGA = Field - Goal Attempts
    # FTA = Free Throw Attempts

def UsgRate():
    100 * ((FGA + 0.44 * FTA + TO) * (TMP / 5)) / (MP * (TFGA + 0.44 * TFTA + TTO))
    # FGA = Field - Goal Attempts
    # FTA = Free - Throw Attempts
    # TO = Turnovers
    # TMP = Team Minutes Played
    # MP = Minutes Played
    # TFGA = Team
    # Field - Goal Attempts,
    # TFTA = Team Free Throw Attempts
    # TTO = Team Turnovers

def PPP():
    PT / (FGA + 0.44 * FTA + TO)
    # PT = Points
    # FGA = Field - Goal Attempts
    # FTA = Free - Throw Attempts
    # TO = Turnovers

def ORTg():
    100 * PP / (FGA + 0.44 * FTA + TO)
    # PP = Points Produced
    # FGA = Field - Goal Attempts
    # FTA = Free - Throw Attempts

def OFFWinSh():
    (PP - 0.92 * LPPP * (FGA + 0.44 * FTA + TO)) / (0.32 * LPPG * (TP / LP))
    # PP = Points Produced
    # LPPP = League Points Per Possession
    # FGA = Field - Goal Attempts
    # FTA = Free - Throw Attempts
    # TO = Turnovers
    # LPPG = League Points Per Game
    # TP = Team Pace
    # LP = League Pace
