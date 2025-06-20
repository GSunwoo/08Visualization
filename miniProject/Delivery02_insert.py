import requests, json
import cx_Oracle as cx

url = 'https://openapi.gg.go.kr/GGEXPSDLV?'
# 오라클 연결
host_name= 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info= cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
# 커서 생성
cursor = conn.cursor()

for page in range(1, 41):
    params = dict(
        Type='json',
        pIndex= page,
        pSize='1000',
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

        sql = """insert into g_deliv (idx, sigun, str, addr, latitude, longitude)
                    values(g_deliv_seq.nextVal, :sigun, :str, :addr, :latitude, :longitude)"""

        try:
            # 커서를 통해 쿼리문 실행
            cursor.execute(sql, sigun=SIGUN_NM, str=STR_NM, addr = REFINE_LOTNO_ADDR,
                           latitude=REFINE_WGS84_LAT, longitude=REFINE_WGS84_LOGT)
            # 실행에 문제가 없다면 커밋해서 실제 테이블에 적용
            conn.commit()
            print('레코드 1개 입력')
        except Exception as e:
            # 예외가 발생했다면 롤백 처리
            conn.rollback()
            print('insert 실행시 오류발생', e)
# DB 연결 해제
conn.close()