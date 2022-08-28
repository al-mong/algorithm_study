'''비행기 종류만 구하면돼서 연결되어 있는 최소값 구하면됨. N-1임'''

import sys

input = sys.stdin.readline
T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(M)]
    print(N-1)