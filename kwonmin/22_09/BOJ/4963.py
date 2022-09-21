import sys

limit_number = 15000

sys.setrecursionlimit(limit_number)

def find_island(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if field[x][y] == 1:
        field[x][y] = 0
        find_island(x-1,y+1)
        find_island(x+1,y-1)
        find_island(x-1,y-1)
        find_island(x+1,y+1)
        find_island(x,y-1)
        find_island(x,y+1)
        find_island(x-1,y)
        find_island(x+1,y)
        return True
    else:
        return False

while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    field = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                find_island(i, j)
                cnt += 1
            else:
                continue
    print(cnt)
