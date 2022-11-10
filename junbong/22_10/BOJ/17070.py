# 221102

'''
어떤 점으로 올 수 있는 위치의 경우의 수들을 전부 더 하면
해당 점의 경우의 수가 된다.

그렇다면 위치 i, j는
왼쪽에서 가로, 위쪽에서 세로, 왼쪽 위에서 대각선 방향으로 올 수 있으므로
dp[i][j] = dp[i][j - 1] + dp[i - 1][j] + dp[i - 1][j - 1] ??
=> X

왼쪽에서 가로로 오려면 왼쪽에서 한 단계 더 전의 위치에서 가로 or 대각선으로 왔어야 한다.
위쪽에서 세로로 오려면 한 단계 전에서 세로 or 대각선으로 왔어야 한다.
마찬가지로 대각선으로 오려면 한 단계 전에서 가로 or 세로 or 대각선으로 왔어야 한다.

그러므로 현재 위치로 올 수 있는 경우의 수를 X라고 하면
X = (가로 유입, 세로 유입, 대각선 유입)
= (가로의 가로 + 가로의 대각선, 세로의 세로 + 세로의 대각선, 대각선의 ~)

벽을 고려할 때는 들어오는 가로, 세로, 대각선 값을 0으로 바꿔주기만 하면 되는데
대각선 파이프는 4칸을 잡아먹는다는 것만 주의하면 된다.
예를 들어 현재 위치에서 위쪽 칸에 벽이 있으면 대각선으로 들어오지 못한다.

마지막 칸에 벽이 있는 경우도 있다.
'''

import sys; input = sys.stdin.readline

N = int(input().rstrip())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[(0, 0, 0) for _ in range(N)] for _ in range(N)]

# 1행 세팅
for j in range(1, N):
    if board[0][j]:
        break
    dp[0][j] = (1, 0, 0)

for i in range(1, N):
    for j in range(2, N):
        hor = dp[i][j - 1][0] + dp[i][j - 1][2]  # 가로
        ver = dp[i - 1][j][1] + dp[i - 1][j][2]  # 세로
        dia = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]  # 대각선
        
        if board[i][j - 1]:  # 왼쪽에 벽이 있을 때
            hor = dia = 0
        if board[i - 1][j]:  # 위쪽에 벽이 있을 때
            ver = dia = 0
        if board[i - 1][j - 1]:  # 왼쪽 위에 벽이 있을 때
            dia = 0

        dp[i][j] = (hor, ver, dia)

if board[N - 1][N - 1]:  # 마지막 칸이 벽인 경우
    dp[N - 1][N - 1] = (0, 0, 0)

print(sum(dp[N - 1][N - 1]))
