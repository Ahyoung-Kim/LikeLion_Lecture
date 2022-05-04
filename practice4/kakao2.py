import os
from dotenv import load_dotenv
import json
import requests

from requests import request

# 환경변수 불러오기
load_dotenv()
rest_api_key = os.getenv("REST_API_KEY")

# 토큰 response를 담은 json파일을 tokens라는 변수로 불러와 저장
with open("kakao_token.json", "r") as json_file:
  tokens = json.load(json_file)

# 우리가 요청을 보낼 url
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 카카오 api 서비스 사용을 위해선 내가 서비스를 이용할 수 있다는 유저임을 인증하기 위한
# authorization 토큰을 요청하는 헤더에 담아서 보내주기
# 이때 tokens의 access_token이라는 키를 가지는 값을 데려와서 값을 넣어주기
headers = {
  "Authorization" : "Bearer " + tokens["access_token"]
}

# 우리가 메세지로 보낼 내용
data = {
  #메모리 상에 JSON 포맷 데이터를 만들어놓고 python에서 계속 작업을 하기 위한 메소드
  "template_object" : json.dumps({ 
    "object_type" : "text", #우리가 보내는 객체의 타입은 text
    "text" : "우리는 서강대 멋사 10기야~", #우리가 보내는 텍스트 내용
    "link" : { #우리가 보낼 링크 주소 (임의로 작성 가능)
      "web_url" : "https://www.instagram.com/likelion_sg"
    }
  })
}

# 요청을 보낼 때 우리가 위에서 변수로 선언한
# 1) 요청 보낼 url 2) 엑세스 토큰이 담긴 헤더 3) 보낼 메시지 (json data)
# 요청을 보내면 그에 대한 응답이 올텐데, 이를 response에 담기
response = requests.post(url, headers=headers, data=data)

# 200이면 요청 성공
print(response.status_code)


if response.json().get('result_code') == 0:
  print('메세지를 성공적으로 보냈습니다!')
else:
  print('메세지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))

  #동의항목이 잘 설정되어 있는지 확인해주기 위해서 수행하는 요청
  # 이 요청을 수행하면 우리가 동의를 요구한 항목들의 상태가 true/false로 나옴
  info_url = 'https://kapi.kakao.com/v2/user/scopes'
  params = {'secure_resource' : True}
  info_res = requests.get(info_url, headers=headers, params=params)
  print(info_res.json())