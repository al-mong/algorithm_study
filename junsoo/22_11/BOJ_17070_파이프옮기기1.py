import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0 for _ in range(3)] for __ in range(n)] for ___ in range(n)]   # [대각선, 가로, 세로]
dp[0][1][1] = 1
# print[dp]

for i in range(2, n - 1):
    if not field[0][i]:
        dp[0][i][1] = 1
    else:
        break

for i in range(1, n):  # 행 번호
    for k in range(2, n): # 열 번호
        if not field[i][k]:
            # 가로 받기
            dp[i][k][1] = dp[i][k-1][0] + dp[i][k-1][1]

            # 세로 받기
            dp[i][k][2] = dp[i-1][k][0] + dp[i-1][k][2]

            if not field[i-1][k] + field[i][k-1]:
                # 대각선 받기
                dp[i][k][0] = dp[i-1][k-1][0] + dp[i-1][k-1][1] + dp[i-1][k-1][2]

# print[dp]
print(sum(dp[n-1][n-1]))