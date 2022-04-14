# 복권 추첨기

import random


def make_lotto():
    lotto = []
    # 1-45 사이의 번호 6개를 랜덤으로 뽑아 lotto 배열에 넣어보세요
    # HINT: random 모듈 사용
    
    while len(lotto) < 6:
        random_num = random.randint(1, 45)
        
        if random_num in lotto:
            continue

        lotto.append(random_num)

    return lotto


def print_lottos(lottos):
    # 뽑은 복권들을 형식에 맞게 출력해보세요
    # HINT: 정렬 함수 사용
    
    for idx, lotto in enumerate(lottos):
        lotto.sort()
        print(idx+1, '번째 복권: ', lotto)
       


while True:
    # 구매할 복권의 개수를 입력받아보세요
    num = input("몇 개의 복권을 구매하시겠습니까?(숫자만 입력하세요): ")

    # 입력값이 숫자가 아닌 경우는 어떻게 처리할 수 있을까요?
    # HINT: 숫자 판별 함수 사용
    if not num.isdigit():
        print("숫자를 입력해주세요.")
        continue

    # 구매할 복권의 개수만큼 복권을 만들어 lottos 배열에 넣어보세요
    lottos = []
    
    for i in range(int(num)):
        lotto = make_lotto()
        lottos.append(lotto)

    print_lottos(lottos)
    break
