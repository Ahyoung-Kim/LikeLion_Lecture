from dotenv import load_dotenv
import os
import requests
import json

#환경 변수 호출
load_dotenv()
rest_api_key = os.getenv("REST_API_KEY")
authorization_code = os.getenv("AUTHORIZATION_CODE")

# 토큰 발급을 해달라고 요청할 url
url = "https://kauth.kakao.com/oauth/token"

# 발급된 토큰을 반환해줄 url
redirect_uri = "http://127.0.0.1"

# 토큰을 발급할 때 카카오가 요구하는 정보들
data = {
  'grant_type' : 'authorization_code',
  'client_id' : rest_api_key, #클라이언트 인증 키
  'redirect_uri' : redirect_uri, #응답을 반환할 url
  'code' : authorization_code #인가 코드
}

# 우리가 설정한 토큰 발급을 요청할 url에, 카카오가 토큰 발급을 위해 
# 필요하다고 한 정보들을 넣어 토큰을 발급해달라는 요청을 보내면
# 돌아올 응답을 response에 담습니다. 
response = requests.post(url, data=data)

# 토큰 발급 응답을 json 형태로 변환해줍니다.
tokens = response.json()

print(tokens)

# kakao_code_json 이라는 이름의 파일을 쓰기 모드로 열어놓고
with open("kakao_token.json", "w") as json_file:
  # json으로 내보내고자 하는 파이썬 객체인 tokens를 직렬화된 데이터가 
  # 쓰여질 파일 json_file 에 쓰기
  json.dump(tokens, json_file)

