## NBA AI Project

The project is still in development.
The Goal of the project is to train an AI on how to grade players and show their future projections.

### To use the project you will need to have these packages installed:
- NBA_API
- pandas
- Scikit-learn 
- numpy
- matplotlib

Run pip install -r requirements.txt to install all necessary packages.  

To create a json file from one of the functions in nba_service use the shell command python -m services.create_json followed by the function name and playerid

Example of shell command to use to get the career stats for the player with player id 2544

```shell
python -m services.create_json get_player_career_stats 2544
```

The json file will be created in the data directory and will be formated with function_name_playerid
