'''
1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.

2-1. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.

2-2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    반시계 방향으로  90도 회전한다.
    바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    1번으로 돌아간다.
'''
# import pprint
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 방의 크기
r, c, d = map(int, input().split()) # 좌표(r,c)와 보는 방향 d(상0, 우1, 하2, 좌3)
D = [(0, -1), (-1, 0), (0, 1), (1, 0)]    # 방향키

ground = []
for i in range(n):
    ground.append(list(map(int, input().split())))

result = 0
while True:
    # pprint.pprint(ground)
    if not ground[r][c]:
        ground[r][c] = 2
        result += 1

    for _ in range(4):
        x, y = D[d]
        if d:
            d -= 1
        else:
            d = 3
        if not ground[r+x][c+y]:
            r, c = r + x, c + y
            break
    else:
        x, y = D[d-1]
        if ground[r + x][c + y] == 1:
            print(result)
            break
        else:
            r, c = r + x, c + y