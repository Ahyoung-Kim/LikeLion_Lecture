import imghdr
import smtplib
from email.message import EmailMessage
import re #파이썬 정규표현식

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# MIME 형태로 변환
message = EmailMessage()
message.set_content('코드라이언 수업중입니다.') #본문

# MIME 형태의 메일의 Header
message["Subject"] = "이것은 제목입니다."
message["From"] = "dkdud6686575@gmail.com"
message["To"] = "ahyoung082799@gmail.com"

def sendEmail(addr):
  #정규표현식
  reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
  #print(re.match(reg, "codelion.example@gmail.com")) #틀렸으면 None

  if bool(re.match(reg, addr)):
    smtp.send_message(message)
    print("정상적으로 메일이 발송되었습니다.")
  else:
    print("유효한 이메일 주소가 아닙니다.")



# 이미지 열고 자동으로 닫아줌
with open("likelion.png", "rb") as image:
  image_file = image.read()

image_type = imghdr.what('e-mail', image_file)
print(image_type)
message.add_attachment(image_file, maintype = 'image', subtype = image_type)


# 1. smtp 서버에 연결하기
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

#print(smtp)

# 2. 서버에 로그인
smtp.login("dkdud6686575@gmail.com", "dkdud0827")


# 3. 서버로 메일 보내기
# smtp는 MIME 형태의 메세지만 읽을 수 있음
#smtp.send_message(message)
sendEmail('ahyoung082799@gmail.com')

# 메세지 보내면 서버와의 연결 끊기 
smtp.quit()
