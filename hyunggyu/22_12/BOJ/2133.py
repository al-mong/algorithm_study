n = int(input())
dp=[0]*(31)
dp[2] = 3
if n < 4:
    pass
else:
    for i in range(4, n+2, 2):
        dp[i] = 3 * dp[i-2]
        for j in range(4, i, 2):
            dp[i] += 2 * dp[i-j]
        dp[i] += 2
print(dp[n])
# N : 2 ANS : 3
# N : 4 ANS : 11 3*3 +0 +2
# N : 6 ANS : 41 11*3 + 2*3 +2
# N : 8 ANS : 153 41*3 + 2*(3+11) +2
# N : 10 ANS : 571 153*3 +2*(3+11+41) +2
# N : 30 ANS : 299303201