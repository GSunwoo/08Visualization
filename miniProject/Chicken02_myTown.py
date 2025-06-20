import squarify
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = '../resData/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_csv('../saveFiles/종로_치킨집.csv',)

num_chk_df = df['지역'].value_counts().reset_index(name='개수').rename(columns={'index': '지역'})
print(num_chk_df)

plt.style.use('ggplot')
plt.figure(figsize=(20,15))
num_chk_df['label'] = num_chk_df['지역'] + '('+num_chk_df['개수'].astype(str) +')'
squarify.plot(sizes=num_chk_df['개수'], label=num_chk_df['label'], alpha=.8)
plt.axis('off')
plt.show()