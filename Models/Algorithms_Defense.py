#NOTE: Might not need math
import math
import numpy as np

# TODO: Write all the defensive algorithms
def StlPerc():
    100 * (S * (TMP / 5)) / (MP * OP)
    # S = Steals
    # TMP = Team Minutes Played
    # MP = Minutes Played
    # OP = Opponents Possessions

def BlkPerc():
    100 * (B * (TMP / 5)) / (MP * (OFGA - O3PA))
    # B = Blocks
    # TMP = Team Minutes Played
    # MP = Minutes Played
    # OFGA = Opponent Field Goal Attempts
    # O3PA = Opponent Three Point Attempts

def DefRebPerc():
    100 * (DRB * (TMP / 5) / (MP * (TORB + ODRB))
