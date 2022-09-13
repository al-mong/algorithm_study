# 계단 오르기
# 두계단까지 올라갈수 있다!
# 마지막 계단은 밟아야한다.
# 3개 연속 밟을수는 없다.
# 계단 최대는 300개
n = int(input())
step = [0 for _ in range(301)]
# dp는 n까지의 최대값을 의미
dp = [0 for _ in range(301)]
dp[0] = step[0]
dp[1] = step[0] + step[1]
dp[2] = max(step[1] + step[2], step[0] + step[2])
for i in range(3,n):
    # 2계단 2계단 밟는게 더 의미있는 경우는 어떻게 할까?
    # -> 2계단 밟고 1계단 오른것과 그다음 dp에서 2계단 오른것을 비교
    dp[i] = max(dp[i-3] + step[i-1] +step[i], dp[i-2] + step[i])
print(dp[n-1])