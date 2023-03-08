# 시키는 대로 하는 문제

from sys import stdin; input=stdin.readline

N, M = map(int,input().split())

sx, sy, d = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

cnt = 0

while True:
    if field[sx][sy] == 0:
        field[sx][sy] = -1
        cnt += 1
    
    if field[sx-1][sy] != 0 and field[sx+1][sy] != 0 and field[sx][sy+1] != 0 and field[sx][sy-1] != 0:
        if field[sx + dx[(d+2)%4]][sy + dy[(d+2)%4]] == 1:
            break
        else:
            sx = sx + dx[(d+2)%4]
            sy = sy + dy[(d+2)%4]
            continue
    else:
        d = (d+3)%4
        if field[sx+dx[d]][sy+dy[d]] == 0:
            sx = sx+dx[d]
            sy = sy+dy[d]
            continue

print(cnt)