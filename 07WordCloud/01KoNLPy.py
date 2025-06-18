from konlpy.tag import Okt

test = ('동해물과 백두산이 마르고 닳도록'
        '하느님이 보우하사 우리나라 만세 Korea ^^')

okt = Okt()

print(okt.morphs(test))

print(okt.nouns(test))

result1 = okt.phrases(test)
print(result1)

result2 = okt.pos(test)
print(result2)
