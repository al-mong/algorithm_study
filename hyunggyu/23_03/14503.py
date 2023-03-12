# n*m의 크기 공간으로 구성
# 지도는 r*c로 나타내고 r은 북으로 부터 떨어진 칸의 개수, c는 서로 부터 떨어진 칸의 개수
# 서, 북, 동 -> 청소할곳없으면 후진 
# 4방향 모두 청소되고, 뒤쪽이 벽인 경우 작동 정지

# 방향에 따른 기준이 rotate로 돌아야될것 같다.
from collections import deque
# 방의 크기(3~50) 세로 n 가로 m
n, m = map(int,input().split())
# 로봇의 좌표r, c와 바라보는 방향d 
# 0은 북, 1은 동, 2는 남, 3은 서
r, c, d = map(int, input().split())
# room = 방
room = [(list(map(int,input().split()))) for _ in range(n)]
# 방향을 정할 기준
law = [(-1,0),(0,1),(1,0),(0,-1)] # 좌하우상 -> 1이면 -> 상좌하우
# law는 정해진 인덱스를 기준으로 계속 회전해야한다.
# 빈칸은 0 벽은 1로 주어진다.
law = deque(law)
law.rotate(d)
result = 1
ending = True
# 간곳은 2로 표기하자
room[r][c] = 2
while ending:
    cnt = -1
    back = False
    for i in range(4):
        cc, rr = c + law[i][0], r + law[i][1]
        if room[rr][cc] == 0:
            r, c = rr, cc
            room[r][c] = 2
            result += 1
            break
        elif cnt == -4 and room[rr-law[i][1]*2][cc-law[i][0]*2] == 2:
            back = True
            r, c = rr-law[i][1]*2, cc-law[i][0]*2
            break
        elif cnt == -4 and room[rr-law[i][1]*2][cc-law[i][0]*2] == 1:
            ending = False           
            break
        cnt -= 1
    if cnt == -4 and back:
        cnt = 0
    law.rotate(cnt)
print(result)