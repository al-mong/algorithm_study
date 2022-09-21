'''런타임에러가 나서 찾아보니 파이썬의 재귀 최대 깊이의 기본 설정이
1,000회라서 런타임에러가 나는 경우가 대부분이라함.
그래서 sys.setrecursionlimit(10**9) 해줘야함'''

import sys
sys.setrecursionlimit(10**9)


# 4가지 방향 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 깊이우선탐색, 재귀로 # 있는 곳 다 탐색하게 만듬
# 이때, 재귀라서 더이상 탐색할 곳 없으면 다시 원래 자리로 돌아옴

def dfs(x, y):
    g[x][y] = '.'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and g[nx][ny] == '#':
            dfs(nx, ny)


T = int(input())
for i in range(T):
    H, W = map(int, input().split())
    g = []
    for i in range(H):
        list1 = list(input())
        g.append(list1)
    cnt = 0
    # 자리에 '#' 이 있으면 dfs 탐색하고 cnt 에 1 추가하기
    for i in range(H):
        for j in range(W):
            if g[i][j] == '#':
                dfs(i, j)
                cnt += 1
    print(cnt)