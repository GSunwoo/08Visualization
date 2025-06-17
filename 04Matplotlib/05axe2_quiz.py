import pandas as pd
import matplotlib.pyplot as plt
from  matplotlib import font_manager, rc

font_path = '../resData/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine='openpyxl', header=0)
df = df.fillna(method='ffill')
mask = (df['전출지별']=='강원도')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지',inplace=True)
sr_one = df_seoul.loc['서울특별시', '1980':]

# sr_one = sr_one.drop(sr_one.index[0:10])

plt.style.use('ggplot')
fig = plt.figure(figsize=(20,5))
ax1 = fig.add_subplot(2,1,1)

ax1.plot(sr_one, marker='o', markersize=10, markerfacecolor='orange', color='olive', linewidth=2 ,label='강원도->서울')
ax1.legend(loc='best')
ax1.set_ylim(10000,80000)
ax1.set_title('강원 -> 서울 인구 이동', size=20)
ax1.set_xlabel('기간',size=12)
ax1.set_ylabel('이동인구수',size=12)
ax1.set_xticklabels(sr_one.index, rotation=70)

ax1.tick_params(axis='x', labelsize=10)
ax1.tick_params(axis='y', labelsize=10)

plt.show()