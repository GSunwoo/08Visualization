import matplotlib.pyplot as plt
import seaborn as sns

# 씨본에서 제공하는 타이타닉 데이터셋 로드
titanic = sns.load_dataset('titanic')
# 스타일 테마 설정
sns.set_style('darkgrid')

'''
히트맵 : 열을 뜻하는 Heat와 지도를 뜻하는 Map을 결합한 단어로
    색상으로 표현할 수 있는 다양한 정보를 일정한 이미지 위에
    열분포 형태의 비쥬얼한 그래픽으로 출력한다.
'''

'''
데이터프레임을 피벗테이블로 정리할때 성별(sex)를 행 인덱스로
죄석등급(class)를 열의 이름으로 설정한다. aggfunc 옵션은 데이터값의
크기를 기준으로 집계한다는 의미.'''
table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size')

'''
히트맵 그리기
    table : 데이터프레임을 피봇테이블로 정리한 변수
    anoot : 데이터값 표시 여부(False면 표시하지 않음)
    fmt : 정수형(d) 포맷으로 설정
    cmap : 컬러맵
    cbar : 컬러바 표시여부(False면 표시하지 않음)
'''
sns.heatmap(table, annot=True, fmt='d', cmap='YlGnBu', linewidths=.5,cbar=True)

plt.show()