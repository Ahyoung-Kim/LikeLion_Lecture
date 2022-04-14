# 성적 계산기

students = {20111111: ['호랑이', 92, 85, 65], 20101234: ['사자', 100, 90, 75],
            20124321: ['토끼', 95, 90, 90], 20135555: ['여우', 55, 60, 65]}


def add():
    id = int(input("학번을 입력하세요: "))

    # 이미 등록된 학생의 학번이 입력된 경우는 어떻게 확인할 수 있을까요?
    if id in students.keys():
        print("이미 입력된 학생입니다.")
        return

    # 학생의 이름과 국영수 성적을 입력받아 등록해주세요
    name = input("이름을 입력하세요: ")
    korean = int(input("국어성적을 입력하세요: "))
    english = int(input("영어성적을 입력하세요: "))
    math = int(input("수학성적을 입력하세요: "))

    students[id] = [name, korean, english, math]

    print("학생의 성적을 입력했습니다.")


def delete():
    id = int(input("삭제하기 원하는 학생의 학번을 입력하세요: "))

    # 없는 학생의 학번이 입력된 경우는 어떻게 확인할 수 있을까요?
    if id not in students.keys():
        print("없는 학생입니다.")
        return

    # 학생 정보를 삭제해주세요
    del students[id]

    print("학번: %d 학생의 정보를 삭제했습니다." % id)


def print_all():
    print("-" * 50)

    # 학생들의 성적을 포맷에 맞게 출력해주세요
    # 성적의 평균을 구해 함께 출력해주세요
    id_list = students.keys()
    for id in id_list:
        values = students.get(int(id))
        name = values[0]
        ko = values[1]
        en = values[2]
        ma = values[3]
        score = values[1:]
        avg = int(sum(score)/len(score))
        print('학번: ', id, '이름: '+name, '   | 국어: ', ko,
            ' / 영어: ', en, ' / 수학: ', ma, ' / 평균: ', avg)

    print("-" * 50)


while True:
    print()
    print("1. 추가, 2. 삭제, 3. 출력, 4. 종료")
    num = int(input("숫자를 선택하세요: "))
    print()

    # 조건문을 채워 넣어 주세요!
    if num == 1:
        add()
    elif num == 2:
        delete()
    elif num == 3:
        print_all()
    else:
        break
