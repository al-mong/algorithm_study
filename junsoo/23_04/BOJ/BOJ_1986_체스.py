n, m = map(int, input().split())
queen, *q = map(int, input().split())   # 가로, 세로, 대각선 무한이동
knight, *k = map(int, input().split())  # 2*3 네모의 반대꼭지점 이동
pawn, *p = map(int, input().split())    # 단순 장애물

# 세팅
ground = [[0 for _ in range(m)] for _ in range(n)]  # n*m 체스판
for i in range(queen):
    x, y = q[i*2] - 1, q[i*2 + 1] - 1
    ground[x][y] = 'q'
for i in range(knight):
    x, y = k[i*2] - 1, k[i*2 + 1] - 1
    ground[x][y] = 'k'
for i in range(pawn):
    x, y = p[i*2] - 1, p[i*2 + 1] - 1
    ground[x][y] = 'p'


# queen 돌면서 확인
dq = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
wall = {'q', 'k', 'p'}
for i in range(queen):
    x, y = q[i*2] - 1, q[i*2 + 1] - 1
    for d in dq:
        dx, dy = x, y   # 초기화
        while True:
            dx += d[0]
            dy += d[1]
            if 0 <= dx < n and 0 <= dy < m:
                if ground[dx][dy] in wall:   # 장에물에 막히면 멈춤
                    break
                if not ground[dx][dy]:  # 1로 채우기
                    ground[dx][dy] = 1
            else:
                break

# knight 돌면서 확인
dk = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
for i in range(knight):
    x, y = k[i*2] - 1, k[i*2 + 1] - 1
    for d in dk:
        dx, dy = x + d[0], y + d[1]   # 초기화
        if 0 <= dx < n and 0 <= dy < m:
            if not ground[dx][dy]:  # 1로 채우기
                ground[dx][dy] = 1
        else:
            continue

result = 0
for i in range(n):
    for j in range(m):
        if not ground[i][j]:
            result += 1
print(result)