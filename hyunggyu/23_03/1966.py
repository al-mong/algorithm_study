import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import defaultdict
    

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    note = list(map(int, input().split()))
    check = [0 for _ in range(10)]
    for new in note:
        check[new] += 1
    # print(check)
    now = 0 # 처음부터 보고
    check_now = 9 # 가장 높은 중요도 9
    result = 0
    while True:
        # 본 곳은 0으로 만든다.
        if note[now] > 0: # 인쇄된 문서가 아니고
            while check_now > 0 and not check[check_now]: # 해당 문서가 없으면
                check_now -= 1
            # print('check_',check_now)
            if check_now == note[now]: # 가장 중요도가 높으면
                check[check_now] -= 1
                note[now] = 0
                result += 1
        if note[M] == 0:
            break
        now += 1
        if now >= N:
            now = 0
    # print(check)
    print(result)
        