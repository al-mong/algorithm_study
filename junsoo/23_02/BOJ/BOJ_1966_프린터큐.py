import sys

input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())  # 문서 개수, 원하는 문서
    num_que = deque(map(int, input().split()))  # 중요도 큐

    important = {i: 0 for i in range(1, 10)}  # 1 ~ 9

    for num in num_que:
        important[num] += 1

    maximum = 9
    while True:
        if important[maximum]:
            break
        maximum -= 1

    result = 0
    while True:
        q = num_que.popleft()
        if q < maximum: # 중요도보다 낮을 때
            num_que.append(q)
            if m == 0:  # 지금 문서가 원하는 문서이면
                m = n - 1   # 큐 끝으로 이동
            else:
                m -= 1
        else:           # 중요도와 같을 때
            result += 1
            n -= 1
            important[maximum] -= 1

            if m == 0:  # 지금 문서가 원하는 문서이면
                print(result)
                break
            else:
                m -= 1

            while True:
                if important[maximum]:
                    break
                maximum -= 1