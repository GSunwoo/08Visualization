import pandas as pd
import matplotlib.pyplot as plt
from  matplotlib import font_manager, rc

# 한글 깨짐방지 설정
font_path = '../resData/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 엑셀을 데이터프레임으로 전환
df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine='openpyxl', header=0)
df = df.fillna(method='ffill')
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지',inplace=True)
sr_one = df_seoul.loc['경기도']
cs_one = df_seoul.loc['충청남도']
kb_one = df_seoul.loc['경상북도']
# kw_one = df_seoul.loc['강원도']

# 스타일 설정 및 Axe객체 1개 생성
plt.style.use('ggplot')
fig = plt.figure(figsize=(20,5))
ax1 = fig.add_subplot(1,1,1)
'''
map 함수를 통해 1970~2017까지의 문자열로 구성된 리스트를 생성한다.
map의 첫번째 인수는 str함수이므로 범위만큼 반복하면서 호출하게 된다.'''
col_years = list(map(str, range(1970,2018)))

# ax1.plot(sr_one, marker='o', markersize=10, markerfacecolor='orange', color='yellow', linewidth=2 ,label='서울->경기')
'''
1개의 그래프에 3개의 꺾은선을 추가한다.
x축은 기간으로 설정
y축은 해당 행의 전체기간을 선택'''
ax1.plot(cs_one, marker='o', markersize=10, markerfacecolor='green', color='olive', linewidth=2 ,label='서울->충남')
ax1.plot(kb_one, marker='o', markersize=10, markerfacecolor='blue', color='skyblue', linewidth=2 ,label='서울->경북')
ax1.plot(col_years, df_seoul.loc['강원도'], marker='o', markersize=10, markerfacecolor='red', color='magenta', linewidth=2 ,label='서울->강원')

# 범례, 타이틀, 라벨, 기울기 등 설정
ax1.legend(loc='best')
ax1.set_title('서울 -> 충남, 경북, 강원 인구 이동', size=20)
ax1.set_xlabel('기간',size=12)
ax1.set_ylabel('이동인구수',size=12)
ax1.set_xticklabels(sr_one.index, rotation=70)

# 각 축의 눈금 라벨크기 설정
ax1.tick_params(axis='x', labelsize=10)
ax1.tick_params(axis='y', labelsize=10)

plt.show()