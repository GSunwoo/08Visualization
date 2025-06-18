import matplotlib.pyplot as plt
import seaborn as sns

# 씨본에서 제공하는 타이타닉 데이터셋 로드
titanic = sns.load_dataset('titanic')
# 스타일 테마 설정
sns.set_style('whitegrid')

# 그래프의 크기 지정
fig = plt.figure(figsize=(15,5))
# Axe객체는 1행 2열로 지정한 후 가로형으로 2개의 그래프를 표현
axe1 = fig.add_subplot(1,2,1)
axe2 = fig.add_subplot(1,2,2)
'''
stripplot
: 이산형 변수의 데이터 분산을 고려하지 않고 그래프를 출력한다.
  즉, 데이터가 겹쳐지는 경우가 발생한다. x축은 좌석의 등급(class),
  y축은 나이(age)를 사용한다.
swarmplot
: 데이터 분산을 고려하여 데이터가 겹쳐지지 않게 표현한다.
  데이터가 퍼져있는 정도를 입체적으로 볼 수 있다.
'''

sns.stripplot(x='class', y='age', data=titanic, ax=axe1)
sns.swarmplot(x='class', y='age', data=titanic, ax=axe2)

axe1.set_title('Strip Plot')
axe2.set_title('Swarm Plot')

plt.show()