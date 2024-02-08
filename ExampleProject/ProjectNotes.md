## Project Notes

Include pyrightconfig.json in the root directory of you project

# Ensure Downloaded

- pandas
- pyarrow
- numpy
- Scikit-Learn
- matplotlib

## NBA_API Docs

- [Endpoint Docs](https://github.com/swar/nba_api/tree/b25107891ecb86cb385c9dc6c2b79e7c08d31c06/docs/nba_api/stats/endpoints)

Example of how to access a endpoint:

```python
# Here we access the leagueleaders module through endpoints & assign the class to "data"
data = endpoints.leagueleaders.LeagueLeaders()

# Our "data" variable now has built in functions such as creating a dataframe for our data
df = data.league_leaders.get_data_frame()

# Will print the first 5 rows
df.head()
```
