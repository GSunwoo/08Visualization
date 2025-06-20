from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 애국가 텍스트파일 읽어오기
filename = '../resData/박천.txt'
f = open(filename, 'r',encoding='utf-8')
news = f.read()
f.close()

# Okt 객체 선언
okt = Okt()
# 명사만 추출
noun = okt.nouns(news)
new_noun = []

for v in noun:
    # 문자열의 길이가 2이상인 것만 골라 리스트에 추가
    if len(v)>=2:
        new_noun.append(v)
# 각 문자열의 등장 횟수 확인
count = Counter(new_noun)
print('카운트:', count)

noun_list = count.most_common(100)
for v in noun_list:
    print(v)

'''
mask 옵션을 사용하면 사각형이 아닌 다른 모형으로 워드클라우드를 생성할 수 있다.
이미지를 읽고 흰색 배경(255,255,255)를 이미지에서 지워준다.'''
icon = Image.open('../resData/masked01.png').convert('RGBA')
mask_image = Image.new('RGB', icon.size, (255,255,255))
mask_image.paste(icon, icon)
mask_image = np.array(mask_image)

# 워드클라우드 생성(기본 사각형 모양)
# 폰트, 배경색, 가로, 세로 크기 등의 옵션을 설정
wc = WordCloud(font_path='../resData/malgun.ttf',
               background_color='white', colormap='Accent_r',
               width=1000, height=1000, max_words=100, max_font_size=300,
               mask=mask_image, contour_width=3, contour_color='steelblue')

# 텍스트 파일의 내용을 통째로 넘겨주기
wc.generate(news)
wc.to_file('../saveFiles/mask1.png')

# 빈도 데이터 넘겨주기
wc.generate_from_frequencies(dict(noun_list))
wc.to_file('../saveFiles/mask2.png')

plt.show()