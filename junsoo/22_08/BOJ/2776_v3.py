'''
pypy3 기준
339900kb, 2132ms

파이썬3은 시간초과
'''
'''
nlist는 병합정렬
mlist 원소를 이진탐색
'''
'''
1
1
1
3
1 2 1
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

t = int(input())
for i in range(t):
    n = int(input())
    nlist = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    mlist = list(map(int, sys.stdin.readline().split()))

    nlist = merge(nlist)

    for i in mlist:
                                                # [1 2 3 4 5] 5개
        start = 0                               #  s   m   e
        end = len(nlist) - 1                    #  s e
                                                #        s e
        while start <= end:
            mid = (start + end) // 2
            if i < nlist[mid]:              # 찾을 숫자가 중앙 값보다 작을 때
                end = mid - 1
            elif i > nlist[mid]:
                start = mid + 1
            elif i == nlist[mid]:
                print(1)
                break

        if start > end:
            print(0)

'''
차이점이 무엇인지?
함수를 따로 지정 하는 것이 시간 단축의 효과가 있는가?

import sys

def bs(li, n):
    s, e = 0, len(li) - 1
    while s <= e:
        m = (s + e) // 2
        if li[m] == n:
            return 1
        elif li[m] < n:
            s = m + 1
        else:
            e = m - 1
    return 0


for _ in range(int(input())):
    N = int(input())
    li1 = sorted(list(map(int, input().split())))
    M = int(input())
    li2 = list(map(int, input().split()))
    for n in li2:
        print(bs(li1, n))
'''



