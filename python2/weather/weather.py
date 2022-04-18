import requests
import json

city = "Seoul"
apiKey = "92806bfdea6fb89e5c4679d4b54acd23"
lang = 'kr'
units = 'metric' #화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)

data = json.loads(result.text) #str타입을 dict 타입으로

print(data['name'], '의 날씨입니다.')
print('날씨는 ',data['weather'][0]['description'], '입니다.')
print('현재 온도는 ', data['main']['temp'], '입니다.')
print('하지만 체감 온도는 ', data['main']['feels_like'], '입니다.')
print('최저 기온은 ', data['main']['temp_min'], '입니다.')
print('최고 기온은 ', data['main']['temp_max'], '입니다.')
print('습도는 ', data['main']['humidity'], '입니다.')
print('기압은 ', data['main']['pressure'], '입니다.')
print('풍향은 ', data['wind']['deg'], '입니다.')
print('풍속은 ', data['wind']['speed'], '입니다.')