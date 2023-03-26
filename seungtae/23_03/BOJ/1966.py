import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    docs = list(map(int, input().split()))

    ddocs = deque()
    for i in range(len(docs)):
        ddocs.append((docs[i], i))

    maxV = sorted(ddocs, reverse=True)[0][0]

    answer = 0
    while True:
        x, y = ddocs.popleft()
        if x == maxV:
            answer += 1
            if y == m:
                break
            maxV = sorted(ddocs, reverse=True)[0][0]
        else:
            ddocs.append((x, y))
    print(answer)