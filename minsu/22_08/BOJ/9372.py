import sys

T= int(sys.stdin.readline())
for tc in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())

    print(N-1)
