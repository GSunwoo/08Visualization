import pandas as pd
import numpy as np

# csv 파일을 데이터프레임으로 변환
# na_values 옵션으로 결측치 ?를 NaN으로 대체 후 변환
df = pd.read_csv('../resData/auto-mpg.csv', header=None, na_values='?')
# 컬럼 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

# 상위 5개의 데이터 출력하기
print(df.head())
# 마력 컬럼만 출력하기
print(df['horsepower'])

# 문자형 데이터가 포함되어 있으므로 에러 발생됨
# name 컬럼은 자동차의 이름이므로 평균을 계산할 수 없다.
# print(df.mean()) # 주석처리 해야함

print('수치형 열만 선택 후 평균 출력', '='*30)
# numpy 모듈의 number를 이용해서 숫자형인 열만 선택한다.
numeric_df = df.select_dtypes(include=[np.number])
print(numeric_df.mean())
'''
horsepower 컬럼은 na_values가 없을 경우 출력 안됨. ?를 문자로 인식하기 때문
na_valuse가 있을 경우 NaN으로 변경했으므로 컬럼을 숫자형으로 인식해서 포함되어 출력된다.'''

print('연비의 평균 출력','='*30)
print(df['mpg'].mean())

print('연비와 무게 평균 출력','='*30)
print(df[['mpg','weight']].mean())

print('중간값','='*30)
print(df['mpg'].median())
print('제조국가', df['origin'].median())

print('최대값','='*30)
print(df.max())
print('연비',df['mpg'].max())
print('마력', df['horsepower'].max())

print('최소값','='*30)
print(df.min())
print(df['mpg'].min())

print('표준편차','='*30)
print(df['mpg'].std())

print('상관계수','='*30)
print(df[['mpg','weight']].corr())




