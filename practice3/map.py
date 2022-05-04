from urllib import response
from bs4 import BeautifulSoup  #크롤링을 위한 라이브러리
import urllib.request   #URL을 가져오기 위한 라이브러리
from dotenv import load_dotenv  #환경변수를 위한 모듈
# 운영 체제에 등록되어 있는 모든 환경 변수는 os 모듈의 environ
# 이라는 속성을 통해서 접근이 가능하므로 import
import os
import json
import folium
from requests import request

# .env에 우리가 저장한 환경변수 불러오기
load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_key = os.environ.get("CLIENT_KEY")


def make_issac_list():
  # 이삭 토스트 페이지 url
  url = 'http://www.isaacs.co.kr/bbs/board.php?bo_table=branches&page='

  page_num = 2 # 내가 불러오고 싶은 마지막 페이지 + 1의 수
  issac_list = [] # 이삭 매장 주소를 담아올 리스트

  for i in range(1, page_num):
    # url + 숫자
    sourcecode = urllib.request.urlopen(url+str(i)).read()
    # 데이터 파싱
    soup = BeautifulSoup(sourcecode, 'html.parser')

    # 주소는 <td> 태그의 'td_subject'라는 클래스 이름으로 있음
    for j in soup.find_all('td', 'td_subject'):
      temp_text = j.get_text()

      issac_list.append(temp_text)

  return issac_list

#print(make_issac_list())

def search_map(search_text):
    # search_text에는 도로명 주소 하나씩이 담기게 됨
    # 이 도로명 주소 문자열에서 특수 문자를 문자열로 변환해서 반환
    encText = urllib.parse.quote(str(search_text))

    # geocode를 부탁해~ 라고 request를 보낼 url로 geocode를 수행해줄 네이버 api 설정
    url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='+encText
    # request를 보낼 타겟을 위에서 지정한 url로 설정
    request = urllib.request.Request(url)
    # request를 보내며 geocode 해주길 요청할 때 request의 헤더에 우리는 너희 api를 사용할
    # 자격이 있음을 증멸한 인증값을 같이 주기 
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_key)

    # 네이버 geocode url 에 보낸 요청에 대한 응답
    # 응답으로 온 url을 urllib라는 url을 가져와주는 아이를 이용해 열어준 뒤 값 받아오기
    response = urllib.request.urlopen(request)
    # 응답이 잘 왔으면 200
    rescode = response.getcode()
    if(rescode==200):
        # 응답코드가 정상적이면 resopnse를 돌려주고
        response_body = response.read()
        # 사람이 인식할 수 있는 형태인 utf-8 로 복호화해서 리턴
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)


def make_location(issac_list):
    # 경도와 위도를 담을 리스트 
    x = []
    y = []
    for issac_location in issac_list: # 주소 하나씩
        # 각 도로명 주소를 search_map에 넣어주면 geocoding을 수행해 돌려줌
        temp_map = search_map(issac_location)
        # 이 값을 json으로 변환하여 저장
        temp_map = json.loads(temp_map)

        # temp_map을 geocoding된 결과 값들 중에서 addres라는 키값을 가진 배열의
        # 0번째 인덱스 값으로 갱신
        # 이렇게 geocoding 된 temp_node 는 위도, 경도만을 가지는게 아닌
        # address라는 배열의 0번째 인덱스에서 x, y 값으로 경도와 위도를 가지게 됨
        try:
            temp_map = temp_map['addresses'][0]
            x.append(float(temp_map['x']))
            y.append(float(temp_map['y']))
        except IndexError:
            pass
    return x, y

'''issac_list = make_issac_list()
print(issac_list)
x_list, y_list = make_location(issac_list)
print(x_list)
print(y_list)'''

# map_osm과 make_location에서 만든 x, y리스트 전달
def make_marker(map_osm, x, y):
  # 리스트의 인덱스
  for i in range(len(x)):
    # y에 있는 위도와 x에 있는 경도를 map_osm에 마커로 찍히게 더해줌
    # folium.Marker([위도, 경도]).add_to(추가할 folium 지도)
    folium.Marker([y[i], x[i]]).add_to(map_osm)


if __name__ == "__main__" :

  issac_list = make_issac_list()
  x_list, y_list = make_location(issac_list)

  # folium map을 띄어줌. 이렇게 디폴트 값으로 만들면 전 세계 지도가 띄어짐
  map_osm = folium.Map()
  # 우리나라 위도, 경도로 folium map을 띄어주면 우리나라 기준으로 지도가 뜸
  map_osm = folium.Map(location=[37.4729081, 127.039306])

  # 우리가 정한 folium 지도, 경도, 위도 리스트를 전달해
  # map_osm이라는 지도에 마커가 찍히게 해줌
  make_marker(map_osm, x_list, y_list)

  # 우리가 만든 map 을 issac.html 이라는 파일에 저장 후, 실행
  map_osm.save('issac.html')