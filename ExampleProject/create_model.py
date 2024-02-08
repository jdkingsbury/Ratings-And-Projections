import numpy as np
import nba_service as nba
import sklearn.linear_model as linear_model

df = nba.get_league_leaders()

x, y = df.FGA/df.GP, df.PTS/df.GP

x = np.array(x).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)

model = linear_model.LinearRegression()
model.fit(x, y)

r2 = round(float(model.score(x,y)), 2)
predicted_y = model.predict(x)
