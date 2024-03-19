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
- cumestatsplayer

## Weight Differential

- Offense will outweigh defense

## Todos

- [x] Rewrite and remove unnecessary algorithms.
- [ ] Determine if we need to change or add more api calls.

  - [x] Create a file that will create json files for each nba_service function so we will be able to automate making api calls to get the correct data

- [ ] Need to create a base algorithm to create a grade.

  - [ ] need to retrieve the needed stats for the player grade
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

```python
Player Grade=(a×PPG)+(b×RPG)+(c×APG)+(d×SPG)+(e×BPG)−(f×TOV)+(g×FG%)+(h×3P%)+(i×FT%)
```

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

Example on how to use the functions in nba_service to get json data

- If you create file and it has a player id then it will create the json file with the function name of the function you used in nba_service and the playerid
- All files are treated as modules should you should use the command python -m and then services.create_json and then the function name you want to use and the player id

Example of shell command to use to insert all players from a json into the database. The json file is created with the function name of get_all_players in the nba_service file followed by the season year.

```shell
python -m db.insert_data get_all_players 2023-24
```

Example of shell command to use to get the career stats for the player with player id 2544

```shell
python -m services.create_json get_player_career_stats 2544
```

Example of shell command to get all the game logs for a season for a particular player

```shell
 python3 -m services.create_json get_player_game_log 2544 2023-24
```
