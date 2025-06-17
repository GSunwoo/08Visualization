# 데이터프레임 사용을 위한 모듈
import pandas as pd
# 데이터 시각화를 위한 모듈
import matplotlib.pyplot as plt

# 한글깨짐 처리를 위해 폰트매니저 임포트
from  matplotlib import font_manager, rc
# 폰트 경로 설정
font_path = '../resData/malgun.ttf'
# 폰트 파일의 이름을 속성으로 지정
font_name = font_manager.FontProperties(fname=font_path).get_name()
# 폰트 적용
rc('font', family=font_name)

df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine='openpyxl', header=0)

df = df.fillna(method='ffill')
print(df.head())

mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지',inplace=True)
print(df_seoul)
sr_one = df_seoul.loc['경기도']
print(sr_one)

plt.style.use('ggplot')
plt.figure(figsize=(14,5))
plt.xticks(rotation=45)
plt.plot(sr_one.index, sr_one.values, marker='o',markersize=10)
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.legend(labels=['서울->경기'], loc='best', fontsize=15)

# y축에 표시할 데이터의 범위를 지정(최소값, 최대값)
plt.ylim(50000,800000)

'''
위치를 나타내는 x, y좌표에서 x는 인덱스 번호를 사용한다. (0:1970, 1:1971...)
y는 인구수를 나타내는 숫자이므로 그대로 사용할 수 있다.
즉(2,290000)이라면 1972년의 29만의 좌표값이 된다.
'''
# 첫번째 화살표
plt.annotate('', # 텍스트로 표시(화살표이므로 생략)
             xytext=(2, 290000), # 화살표의 꼬리부분(시작점)
             xy=(20,620000),     # 화살표의 머리부분(끝점)
             xycoords='data',    # 좌표체계(데이터를 사용함)
             # 화살표의 스타일 지정. 모양, 컬러, 두께를 딕셔너리로 지정.
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=2))

plt.annotate('',
             xytext=(30, 580000),
             xy=(47,450000),
             xycoords='data',
             arrowprops=dict(arrowstyle='->', color='olive', lw=5))

'''
va : 글자를 위아래 세로(수직) 방향으로 정렬.
     속성값은 center, top, bottom, baseline 등
ha : 글자를 좌우(수평) 방향으로 정렬.
     속성값은 center, left, right 등
'''
plt.annotate('인구이동 증가(1970-1995)',
             xy=(10, 450000), # 텍스트의 위치
             rotation=25,     # 회전각도
             va='baseline',   # 수직방향 정렬
             ha='center',     # 수평방향 정렬
             fontsize=15,     # 텍스트의 크기
             )

plt.annotate('인구이동 증가(1995-2017)',
             xy=(39, 540000),
             rotation=-10,
             va='baseline',
             ha='center',
             fontsize=15,
             )
plt.show()