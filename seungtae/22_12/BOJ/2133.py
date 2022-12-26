import sys

n = int(sys.stdin.readline())
dp = [0] * 31
dp[2] = 3
dp[4] = 11

for i in range(6, n+1, 2):
    dp[i] = dp[i-2]*4 - dp[i-4]     # 점화식
print(dp[n]) 