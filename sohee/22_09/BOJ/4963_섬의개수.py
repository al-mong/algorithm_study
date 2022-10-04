import sys
sys.setrecursionlimit(10**9)

# 대각선까지 8가지 방향 탐색
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(x, y):
    isl[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and isl[nx][ny] == 1:
            dfs(nx, ny)

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:  # 둘 다 입력 0 들어오면 break
        break
    isl = []
    for i in range(H):
        list1 = list(map(int, input().split()))
        isl.append(list1)
    cnt = 0
    # 자리에 1 이 있으면 dfs 탐색하고 cnt 에 1 추가하기
    for i in range(H):
        for j in range(W):
            if isl[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)