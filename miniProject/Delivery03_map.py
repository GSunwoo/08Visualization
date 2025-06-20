import cx_Oracle as cx
import folium

# 오라클 연결
host_name= 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info= cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
# 커서 생성
cursor = conn.cursor()

# 폴리엄으로 지도 생성
univ_map = folium.Map(location=[37.40,127.8], zoom_start=10)
univ_map.save('../saveFiles/deliv_map.html')

select_sigun = input('확인할 지역을 입력해주세요')

# 지도 데이터를 오름차순 정렬해서 인출
sql = 'select * from g_deliv order by idx asc'
cursor.execute(sql)
for rs in cursor:
    if(rs[1]==select_sigun):
        idx = rs[0]
        sigun = rs[1]
        str = rs[2]
        addr = rs[3]
        latitude = rs[4]
        longitude = rs[5]
        folium.Marker([latitude,longitude], popup=str).add_to(univ_map)
        print(str,latitude,longitude)
# 마커가 포함된 지도 생성 및 저장
univ_map.save('../saveFiles/deliv_map_marker_'+select_sigun+'.html')
print('맵이 생성되었습니다.')