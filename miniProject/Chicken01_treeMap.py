import squarify
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = '../resData/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

data = {'customers':[8,3,4,2],
        'cluster':['A','B','C','D']}
df = pd.DataFrame(data)

plt.style.use('ggplot')

df['label'] = df['cluster'] + '\n('+df['customers'].astype(str) +')'
squarify.plot(sizes=df['customers'], label=df['label'], alpha=.8)
plt.axis('off')
plt.show()