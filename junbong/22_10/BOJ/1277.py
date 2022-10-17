# 221014
import sys; input = sys.stdin.readline


def dijkstra(s):
    U = [0] * (N + 1)
    U[s] = 1
    for i in range(1, N + 1):
        D[i] = board[s][i]

    for _ in range(N - 1):
        minV = 300000
        w = 0
        for i in range(1, N + 1):
            if U[i] == 0 and 0 <= D[i] < minV:
                minV = D[i]
                w = i
        U[w] = 1
        for v in range(1, N + 1):
            if 0 <= board[w][v] <= M:
                D[v] = min(D[v], D[w] + board[w][v])


N, W = map(int, input().split())
M = float(input().rstrip())
points = [()] + [tuple(map(int, input().split())) for _ in range(N)]
board = [[-1] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if i != j:
            board[i][j] = board[j][i] = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** (1/2)

for _ in range(W):
    a, b = map(int, input().split())
    board[a][b] = board[b][a] = 0

D = [-1] * (N + 1)
dijkstra(1)
print(int(D[N] * 1000))
