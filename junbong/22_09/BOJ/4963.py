# 220920

import sys
sys.setrecursionlimit(10000)


def dfs(i, j):
    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and board[ni][nj] and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj)


input = sys.stdin.readline
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit()
    board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    result = 0
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                result += 1
                dfs(i, j)

    print(result)
