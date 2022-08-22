'''
pypy기준

718052kb 5376ms

파이썬3
시간초과
'''

'''
수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때,
앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

'''

import sys

def merge(input_list):  # 병합 정렬 재귀 형식
    if len(input_list) == 1:
        return input_list
    elif len(input_list) == 2:
        if input_list[0] > input_list[1]:  # 앞이 크면 뒤집어 준다.
            input_list[0], input_list[1] = input_list[1], input_list[0]
            return input_list
        else:
            return input_list
    else:  # 길이가 3 이상일 떄
        left = input_list[:len(input_list) // 2]
        right = input_list[len(input_list) // 2:]
        left = merge(left)  # left 오름차순 정렬
        right = merge(right)  # rigth 오름차순 정렬

        new_list = [0 for i in range(len(input_list))]  # 새 값을 받아 줄 리스트
        leftnum = left.pop()
        rightnum = right.pop()
        for i in range(len(new_list) - 1, -1, -1):  # 뒤에서 뽑아 쓰니깐 뒤에서부터 집어넣는다
            if leftnum < rightnum:  # 큰놈을 new_list 뒤에 넣는다
                new_list[i] = rightnum
                if len(right) > 0:
                    rightnum = right.pop()
                else:  # right를 다 썼으면 left를 앞에 붙임
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


n, k = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))

alist = merge(alist)
print(alist[k-1])