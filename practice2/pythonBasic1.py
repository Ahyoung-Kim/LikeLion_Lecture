# 문자열 다루기

string_input = "  abcd ,    abcd  "

# 문자열을 콤마를 기준으로 나누어 각각 저장해보세요
'''comma = string_input.find(',')
str1 = string_input[:comma]
str2 = string_input[comma+1:]'''
str1, str2 = string_input.split(',')

# 두 개의 문자열이 가진 앞뒤 공백을 제거해볼까요?
str1 = str1.strip()
str2 = str2.strip()

# 두 개의 문자열이 같은지 비교하여 결과를 출력해보세요
if str1 == str2:
  print(str1+', '+str2+'는 같은 문자열입니다.')
else:
  print(str1+', '+str2+'는 다른 문자열입니다.')

# 다시 두 개의 문자열을 합쳐 하나의 문자열로 만드세요
str3 = str1 + str2

# 합친 문자열의 길이를 출력해보세요
print(str3+'의 길이는 ',len(str3), '입니다.')

