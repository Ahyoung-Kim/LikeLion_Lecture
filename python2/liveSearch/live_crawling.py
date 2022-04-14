import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.nate.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

file1 = open("nate.html", "w", encoding="UTF-8")
file1.write(response.text)
file1.close()

#print(response.text)
#print(soup.title)

#html 문서에서 모든 a 태그를 가져오는 코드
results = soup.findAll("span", "txt_rank")
ranks = soup.findAll("span", "num_rank")

file2 = open("rankresult.txt", "w")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다. \n"))

idx = 0
for result in results:
  rank = ranks[idx].get_text()
  file2.write(rank+"위 : "+result.get_text()+'\n')
  print(rank, "위 : ", result.get_text(), "\n")
  idx += 1
