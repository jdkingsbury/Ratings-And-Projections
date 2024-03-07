# Notes

## How we plan to grade players

- Track players stats through the season
- Track players stats to individual teams
  - We will need to rank teams they play against
  - We will need to rank the players they are matched up against
- Players and teams play style will need to be taken into account

## NBA API Endpoints 

- teamvsplayer
- playervsplayer 
- playergamelogs?
- playerestimatedmetrics
- commonallplayers
- defensehub?

## Weight Differential

- Offense will outweigh defense

## Todos

- [ ] Rewrite and remove unnecessary algorithms.
- [ ] Determine if we need to change or add more api calls.
- [ ] Need to create a base algorithm to create a grade.
  - [ ] Create layers to include other factors which can increase or decrease a players score.
- [ ] Attempt to factor in a players ego.
  - [ ] Check national broadcasted games.
  - [ ] Check how well they match up between certain players.
  - [ ] Check team rivalries and must win games.

## Command Cheat Sheet
- Start Postgres server:
    - brew services start postgresql
- Stop Postgres server:
    - brew services stop postgresql

### Basic Formula

An example set of weights could be:
a=4 (Points are heavily valued)
b=2 (Rebounds contribute to both offense and defense)
c=3 (Assists foster team play and scoring opportunities)
d=1.5 (Steals can indicate defensive prowess and lead to easy points)
e=1.5 (Blocks are an essential part of defense)
f=−2 (Turnovers are negative and thus subtract from the grade)
g=1, h=1, and i=1 (Efficiency in shooting is fundamental)

Player Grade=(a×PPG)+(b×RPG)+(c×APG)+(d×SPG)+(e×BPG)−(f×TOV)+(g×FG%)+(h×3P%)+(i×FT%)

PPG = Points Per Game
RPG = Rebounds Per Game
APG = Assists Per Game
SPG = Steals Per Game
BPG = Blocks Per Game
TOV = Turnovers Per Game
FG% = Field Goal Percentage
3P% = Three-Point Percentage
FT% = Free Throw Percentage
a through i = weights assigned to each statistic based on their perceived importance.
