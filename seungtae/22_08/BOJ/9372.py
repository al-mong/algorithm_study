# 2
# 3 3
# 1 2
# 2 3
# 1 3
# 5 4
# 2 1
# 2 3
# 4 3
# 4 5

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):                            #
    n, m = map(int, input().split())
    adj_dict = {i: [] for i in range(1, n+1)}
    visited = [False] * (1+n)
    for i in range(m):
        x, y = map(int, input().split())
        adj_dict[x].append(y)
        adj_dict[y].append(x)
    q = deque()
    q.append(1)
    visited[1] = True
    count = 0
    while q:
        v = q.popleft()
        for w in adj_dict[v]:
            if not visited[w]:
                visited[w] = True
                q.append(w)
                count += 1
    print(count)
