import requests, json

url = 'https://openapi.gg.go.kr/GGEXPSDLV?'
params = dict(
    Type='json',
    pSize='10',
    KEY='13cec70ac20b450ab658d66751e11f10'
)
raw_data = requests.get(url=url, params=params)
binary_data = raw_data.content
json_data = json.loads(binary_data)

for jd in json_data['GGEXPSDLV'][1]['row']:
    SIGUN_NM = jd['SIGUN_NM']
    STR_NM = jd['STR_NM']
    REFINE_LOTNO_ADDR = jd['REFINE_LOTNO_ADDR']
    REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT']
    REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT']
    print(STR_NM,REFINE_WGS84_LAT,REFINE_WGS84_LOGT)