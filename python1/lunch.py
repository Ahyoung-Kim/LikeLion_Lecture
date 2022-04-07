import random
import time

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

while True:
  food = input("음식을 추가 해주세요(종료: q) : ")

  if food == "q":
    break

  lunch.append(food)


print(lunch)

#list를 set으로 변환
set_lunch = set(lunch)

while True:
  food = input("음식을 삭제 해주세요(종료: q) : ")

  if food == "q":
    break

  #차집합 연산: 겹치는 원소 제거
  set_lunch = set_lunch - set([food])


print(set_lunch, "중에서 선택합니다.")

t = 5

#5초 카운트
while t > 0 :
  print(t)
  time.sleep(1)
  t -= 1

#list에서 랜덤한 원소 뽑기
menu = random.choice(list(set_lunch))
print("오늘의 메뉴는 ",menu, "이다!")