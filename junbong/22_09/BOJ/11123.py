# 220919

'''
for문으로 그래프를 순회하면서
#이 나오면 양 무리 카운트를 1 증가시키고
이어진 #을 전부 탐색
'''

import sys
from collections import deque


def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    while q:
        cur = q.popleft()
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = cur[0] + di, cur[1] + dj
            if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '#' and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1


input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    H, W = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]
    visited = [[0 for _ in range(W)] for _ in range(H)]
    result = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and visited[i][j] == 0:
                result += 1
                bfs(i, j)
    print(result)