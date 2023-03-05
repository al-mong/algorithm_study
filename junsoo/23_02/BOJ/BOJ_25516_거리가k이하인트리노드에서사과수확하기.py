# 0번 정점이 루트
# BFS

import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())

tree = {i: [] for i in range(n)}
for _ in range(n-1):
    p, c = map(int, input().split()) # p = 부모, c = 자식
    tree[p].append(c)

apple = tuple(map(int, input().split()))

que = deque()
for next in tree[0]:    # 0번이 루트
    que.append((next, 1))
# ex) que = deque([(1,0), (2,0)])

result = apple[0]   # 처음 값 = 거리 0인 값 넣기

while que:
    q, length = que.popleft()
    if length <= k:
        result += apple[q]
        for next in tree[q]:
            que.append((next, length+1))

print(result)