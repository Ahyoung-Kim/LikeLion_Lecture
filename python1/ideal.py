total_list = []

while True:
  question = input("질문을 입력해주세요(종료: q) : ")

  if question == "q":
    break

  #리스트의 원소를 딕셔너리로 
  total_list.append({"질문":question, "답변":""})

for i in total_list:
  #i는 하나의 딕셔너리, i[key]=value
  print(i["질문"])
  answer = input("답변을 입력해주세요 : ")
  i["답변"] = answer

print(total_list)