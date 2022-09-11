# 220904

'''
stairs, dp 배열을 생성
stairs[i]: i번째 계단의 점수
dp[i]: i번째(인덱스) 계단을 마지막으로 '밟았을 때' 최대 점수


i번째 계단을 밟기 위해서는
한 번에 두 계단씩 오를 수 있으므로
i - 1번째 또는 i - 2번째 계단에서 올라와야 함


1. i - 1번째 계단을 밟고 i번째 계단을 밟을 때
dp[i] = dp[i - 1] + stairs[i]가 되서는 안됨
dp[i - 1]에는 i - 2번째 계단을 밟은 경우도 포함되어 있을 수 있음
그렇다면 연속해서 세 계단을 밟은 것이기 때문에 유효 x
따라서 i - 2번 째 계단을 밟지 않은 최대값인
dp[i] = dp[i - 3] + stairs[i - 1] + stairs[i]가 되어야 함

2. i - 2번째 계단을 밟고 i번째 계단을 밟을 때의 점수는
dp[i] = dp[i - 2] + stairs[i]

따라서 dp[i]는 1번과 2번의 경우 중 큰 것을 고른다.
마지막 계단을 밟아야 하므로 dp[N - 1]을 출력
'''

import sys

input = sys.stdin.readline
N = int(input().rstrip())
stairs = [int(input().rstrip()) for _ in range(N)]
dp = [0] * N
dp[0] = stairs[0]

if N >= 2:
    dp[1] = stairs[0] + stairs[1]
    
if N >= 3:
    for i in range(2, N):
        dp[i] = stairs[i] + max(dp[i - 2], stairs[i - 1] + dp[i - 3])

print(dp[-1])
