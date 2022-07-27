n = int(input())
for i in range(n):
    ox = input()
    score = 0
    for num, i in enumerate(ox):                    # 문자열 ox를 하나씩 떼서 (순서, 문자)조합으로 생성
        if num == 0:
            if i == 'O':
                ck = 1
            else:
                ck = 0                              # 첫 문제가 맞을 때와 틀릴 때
        else:
            if i == 'O' and ox[num-1] == 'O' :
                ck = ck +1
            elif i == 'O' and ox[num-1] != 'O' :
                ck = 1
            elif i != 'O':
                ck = 0                              # 두 번째 문제부터 연속되면 점수 가산점, 아니면 초기화
        score = score + ck                          # 총합 결과

    print(score)