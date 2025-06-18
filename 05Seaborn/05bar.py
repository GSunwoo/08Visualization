import matplotlib.pyplot as plt
import seaborn as sns

# 씨본에서 제공하는 타이타닉 데이터셋 로드
titanic = sns.load_dataset('titanic')

# 스타일 테마 설정
sns.set_style('whitegrid')

# 3개의 영역으로 구분하기 위해 와이드하게 사지으 지정
fig = plt.figure(figsize=(15,5))
# 수평방향으로 3개의 Axe 객체 생성
axe1 = fig.add_subplot(1,3,1)
axe2 = fig.add_subplot(1,3,2)
axe3 = fig.add_subplot(1,3,3)

'''
barplot ; 막대그래프 생성
    x, y : x, y축에 표시할 데이터
    data : 그래프에 사용할 데이터프레임
    dodge: 데이터 색상을 기준으로 구분할 열 지정
    hue  : 막대그래프를 나란히 배치하거나(True), 겹치도록 배치(False)
'''
sns.barplot(x='sex', y='survived', data=titanic, ax=axe1)
sns.barplot(x='sex', y='survived', hue='class', data=titanic, ax=axe2)
sns.barplot(x='sex', y='survived', hue='class', dodge=False, data=titanic, ax=axe3)

axe1.set_title('titanic survived - sex')
axe2.set_title('titanic survived - sex/class')
axe3.set_title('titanic survived - sex/class(stacked)')

plt.show()