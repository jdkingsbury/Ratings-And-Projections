import create_model
import pyarrow as pa

from matplotlib import pyplot as plt

x = create_model.x
y = create_model.y
r2 = create_model.r2
df = create_model.df
preicted_y = create_model.predicted_y

# Graph 1
plt.scatter(x, y, s=15, alpha=0.5)
plt.plot(x, preicted_y, color='black')
plt.title('NBA - Relationship between FGA and PPG')
plt.xlabel('FGA per game')
plt.ylabel('Points per game')
plt.text(10, 25, f'R2={r2}')

# Graph 2
plt.annotate(df.PLAYER[0], (x[0], y[0]), (x[0]-7,y[0]-2), arrowprops=dict(arrowstyle='-')) 

plt.savefig('graph.png', dpi=300) 

