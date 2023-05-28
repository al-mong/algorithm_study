# 순서대로 위치를 알려줘서, 좀 친절한 문제라고 생각.
# 장애물이 되는 친구들 = 폰과 퀸
# 나이트는 뛰어넘으니까 맨 마지막에 배치
# 폰은 그냥 장애물 역할만 함 (사실 퀸한테 더 방해될지도)
# 순서는 폰 - 퀸 - 나이트 순으로 보면 될 듯.(폰 위치로 퀸의 이동경로가 제한되기 때문)
from sys import stdin; input = stdin.readline
from collections import deque
    


N, M = map(int,input().split())

field = [[0]*M for _ in range(N)]
_, *queens = map(int,input().split())
_, *knights = map(int,input().split())
_, *pawns = map(int,input().split())

dr = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]

for i in range(1,len(pawns), 2):
    x, y = pawns[i-1]-1, pawns[i]-1     # 인덱스가 0이기 때문에 -1 해서 맞춰줌
    field[x][y] = 1                     # 필드 방문처리

# 나이트 처리 시작
k_move = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]

for i in range(1,len(knights),2):
    x, y = knights[i-1]-1, knights[i]-1
    field[x][y] = 1
    for dx, dy in k_move:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M or field[nx][ny] == 1:
            continue
        
        field[nx][ny] = 2



for i in range(1,len(queens), 2):
    # 이제 퀸 처리하기
    x, y = queens[i-1]-1, queens[i]-1
    field[x][y] = 1
    que = deque()
    for i in range(8):
        dx, dy = dr[i]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M or field[nx][ny] == 1:
            continue
        if field[nx][ny] != 1:
            field[nx][ny] = 2
            que.append((nx,ny,i))
    while que:
        x, y, d = que.popleft()
        
        dx, dy = dr[d]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M or field[nx][ny] == 1:
            continue
        if field[nx][ny] != 1:
            field[nx][ny] = 2
            que.append((nx,ny,d))

res = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == 0:
            res += 1

print(res)
