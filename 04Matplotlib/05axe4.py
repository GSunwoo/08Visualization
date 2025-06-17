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
jn_one = df_seoul.loc['전라남도']
kw_one = df_seoul.loc['강원도']

# 스타일 설정 및 Axe객체 1개 생성
plt.style.use('ggplot')
# 그래프 사이즈 지정. 와이드하게 긴 사각형의 형태
fig = plt.figure(figsize=(20,10))
# Axe 객체 생성. 2행 2열의 첫번째부터 순서대로 그래프의 영역을 설정.
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

# range  함수로 1970~2017까지를 반환하면 str 함수를 통해 문자열로 변경한 후 리스트로 생성한다.
col_years = list(map(str, range(1970,2018)))


# ax1.plot(sr_one, marker='o', markersize=10, markerfacecolor='orange', color='yellow', linewidth=2 ,label='서울->경기')

# 각 Axe객체에 plot함수로 그래프를 출력
'''
x축은 1970~2017까지의 연도를 설정. y축은 각 전출지의 전체 데이터를 설정.
나머지는 마커, 컬러, 두께 등을 설정한다.'''
ax1.plot(cs_one, marker='o', markersize=10, markerfacecolor='green', color='olive', linewidth=2 ,label='서울->충남')
ax2.plot(kb_one, marker='o', markersize=10, markerfacecolor='blue', color='skyblue', linewidth=2 ,label='서울->경북')
ax3.plot(col_years, df_seoul.loc['강원도'], marker='o', markersize=10, markerfacecolor='red', color='magenta', linewidth=2 ,label='서울->강원')
ax4.plot(kb_one, marker='o', markersize=10, markerfacecolor='orange', color='yellow', linewidth=2 ,label='서울->전남')

# 범례 설정
ax1.legend(loc='best')
ax2.legend(loc='best')
ax3.legend(loc='best')
ax4.legend(loc='best')

# 타이틀 설정
ax1.set_title('서울 -> 충남 인구 이동', size=20)
ax2.set_title('서울 -> 경북 인구 이동', size=20)
ax3.set_title('서울 -> 강원 인구 이동', size=20)
ax4.set_title('서울 -> 전남 인구 이동', size=20)

# x축 눈금, 회전 설정
ax1.set_xticklabels(sr_one.index, rotation=90)
ax2.set_xticklabels(sr_one.index, rotation=90)
ax3.set_xticklabels(sr_one.index, rotation=90)
ax4.set_xticklabels(sr_one.index, rotation=90)


plt.show()