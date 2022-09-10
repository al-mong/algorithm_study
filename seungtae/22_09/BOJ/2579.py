import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 301
stairs = [0]
for i in range(n):
    stairs.append(int(input()))
if n == 1:
    print(stairs[1])                                                            # n = 1,2,3일 땐 바로 출력
elif n == 2:
    print(stairs[1] + stairs[2])
elif n == 3:
    print(max(stairs[1] + stairs[3], stairs[2] + stairs[3]))
else:
                                                                                # dp 1,2,3 초기화
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

                                                                                # dp 4 이상 부터는 2가지의 케이스 중 큰 것을 고름.
                                                                                # 1. 2칸 전의 계단을 밟고 현재 계단을 밟는 경우
                                                                                # 2. 3칸 전전 계단을 밟고, 1칸전의 계단을 밟고 현재 계단을 밝는 경우
    for i in range(4, n+1):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    print(dp[n])