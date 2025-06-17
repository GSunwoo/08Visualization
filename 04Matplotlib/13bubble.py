import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize

plt.style.use('default')
df = pd.read_csv('../resData/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

cylinders_size= df.cylinders / df.cylinders.max() * 300
print(cylinders_size)

df.plot(kind='scatter', x='weight', y='mpg', c='coral', figsize=(10, 5), s=cylinders_size, alpha=0.3,
        marker='o', cmap='viridis')
plt.title('Scatter Plot : mpg-weight-cylinders')

plt.savefig('../saveFiles/scatter.png')
plt.savefig('../saveFiles/scatter_transparent.png', transparent=True)

plt.show()