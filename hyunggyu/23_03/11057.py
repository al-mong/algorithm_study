import sys
from collections import deque
sys.stdin = open("input.txt")

# 수의 자리가 오름차순을 이루는 수 : 오르막 수(같은거 ㅇㅈ)
dp = list([0]*10 for _ in range(1001))

def ne(n,l):
    if n == 1:
        dp[1][l] = 1
        return dp[1][l]
    if not dp[n][l] == 0:
        return dp[n][l]
    for i in range(l+1):
        dp[n][l] += ne(n-1,i)
    return dp[n][l] % 10007

result = 0
n = int(input())
for i in range(10):
    result += ne(n,i)
print(result % 10007)



