from collections import deque

def 깊이우선탐색(x,y):
    que = deque()
    que.append((x,y))
    field[x][y] = '.'
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if field[nx][ny] == '#':
                que.append((nx,ny))
                field[nx][ny] = '.'

# 양 한마리... 양 두마리...

# 양은 #, 목초지는 .
# '#'을 만나면 .으로 바꾸기
# 방향키 만들자
dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input()) # 테스트케이스 숫자 받기
for _ in range(T):
    N, M = map(int,input().split())
    field = [list(input()) for _ in range(N)]
    res = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == '#':
                깊이우선탐색(i,j)
                res += 1
    print(res)