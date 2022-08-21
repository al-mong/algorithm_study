'''
코드의 문제점
너무 느림 왜?
1. 병합정렬
    1. new_list = left + [leftnum] + new_list[i:] 파트에서 시간을 먹음.
        - 합해서 하는 방법은 아예 없는가?
        - 각자 지정해주는 방법을 사용하면 더 줄이기 가능

    2. 재귀형식
        - 재귀이면 무조건적인가?
        - 바로 재귀를 탈출하는 방법이 있는가?
        - 메모이제이션 사용해서 값이 있으면 바로 종료 - 이건 중간 값에서 끊을 때 사용
        - 재귀의 끝자락에 있으면 차피 거슬러 나와야함

2. 이진탐색
    1. 재귀를 사용하면 매우 느림
        - 바로 재귀를 탈출하는 방법이 있는가? 없으면 while문에 조건을 거는 방법밖에 없나?

    2.


'''

'''
nlist는 병합정렬
mlist 원소를 이진탐색
'''
import sys

def merge(input_list):                                                      # 병합 정렬 재귀 형식
    if len(input_list) == 1:
        return input_list
    elif len(input_list) == 2:
        if input_list[0] > input_list[1]:                                   # 앞이 크면 뒤집어 준다.
            input_list[0], input_list[1] = input_list[1], input_list[0]
            return input_list
        else:
            return input_list
    else:                                                                   # 길이가 3 이상일 떄
        left = input_list[:len(input_list) // 2]
        right = input_list[len(input_list) // 2:]
        left = merge(left)                                                  # left 오름차순 정렬
        right = merge(right)                                                # rigth 오름차순 정렬

        new_list = [0 for i in range(len(input_list))]                      # 새 값을 받아 줄 리스트, 합치기 시작
        leftnum = left.pop()
        rightnum = right.pop()
        for i in range(len(new_list)-1, -1, -1):                            # 뒤에서 뽑아 쓰니깐 뒤에서부터 집어넣는다
            if leftnum < rightnum:                                          # 큰놈을 new_list 뒤에 넣는다
                new_list[i] = rightnum
                if len(right) > 0:
                    rightnum = right.pop()
                else:                                                       # right를 다 썼으면 left를 앞에 붙임
                    new_list = left + [leftnum] + new_list[i:]
                    break
            else:
                new_list[i] = leftnum
                if len(left) > 0:
                    leftnum = left.pop()
                else:
                    new_list = right + [rightnum] + new_list[i:]
                    break

        return new_list


def binary(want, input_list):
    # input_list[len(input_list) // 2]  : 홀수일 땐 중앙, 짝수일 땐 중앙+1
    # input_list는 정렬이 되어 있어야 한다.
    if len(input_list) <= 2:                                # 리스트 길이가 2 이하일 때
        if want in input_list:
            print(1)
        else:
            print(0)
    
    else:
        if want < input_list[len(input_list) // 2]:         # 찾을 숫자가 중앙 값보다 작을 때
            binary(want, input_list[:len(input_list) // 2])

        elif want > input_list[len(input_list) // 2]:       # 찾을 숫자가 중앙 값보다 클 때
            binary(want, input_list[len(input_list) // 2:])
    
        else:                                              # 같을 때
            print(1)                                       # 1 출력




t = int(input())
for i in range(t):
    n = int(input())
    nlist = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    mlist = list(map(int, sys.stdin.readline().split()))

    nlist = merge(nlist)
    for i in mlist:
        binary(i, nlist)
