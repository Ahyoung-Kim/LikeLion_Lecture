from urllib import response
from bs4 import BeautifulSoup  #크롤링을 위한 라이브러리
import urllib.request   #URL을 가져오기 위한 라이브러리
from dotenv import load_dotenv  #환경변수를 위한 모듈
import os
import json
import folium
from requests import request

load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_key = os.environ.get("CLIENT_KEY")


def make_issac_list():
  url = 'http://www.isaacs.co.kr/bbs/board.php?bo_table=branches&page='

  page_num = 2
  issac_list = []

  for i in range(1, page_num):
    sourcecode = urllib.request.urlopen(url+str(i)).read()
    soup = BeautifulSoup(sourcecode, 'html.parser')

    for j in soup.find_all('td', 'td_subject'):
      temp_text = j.get_text()

      issac_list.append(temp_text)

  return issac_list

#print(make_issac_list())

def search_map(search_text):
    encText = urllib.parse.quote(str(search_text))

    url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='+encText
    request = urllib.request.Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_key)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)

def make_location(issac_list):
    x = []
    y = []
    for issac_location in issac_list:
        temp_map = search_map(issac_location)
        temp_map = json.loads(temp_map)
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


def make_marker(map_osm, x, y):
  for i in range(len(x)):
    folium.Marker([y[i], x[i]]).add_to(map_osm)


if __name__ == "__main__" :

  issac_list = make_issac_list()
  x_list, y_list = make_location(issac_list)

  map_osm = folium.Map()
  map_osm = folium.Map(location=[37.4729081, 127.039306])

  make_marker(map_osm, x_list, y_list)

  map_osm.save('issac.html')