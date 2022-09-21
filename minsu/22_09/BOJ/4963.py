"""
섬의 개수를 찾는 문제
가로,세로,대각선으로 이어져 있으면 하나의 섬으로 인식

"""
import sys
sys.setrecursionlimit(10**6)

def dfs(i,j):
    case[i][j] = 0
    di = [0, 1, 0, -1, -1, -1, 1, 1]
    dj = [1, 0, -1, 0, -1, 1, 1, -1]
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < h and 0 <= nj < w:
            if case[ni][nj] == 1:
                dfs(ni,nj)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    case = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if case[i][j] == 1:
                dfs(i,j)
                cnt +=1


    print(cnt)
