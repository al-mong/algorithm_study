import sys
input = sys.stdin.readline

n = int(input())

dp = [[0 for _ in range(3)] for _ in range(n+1)]
dp_ans = [0] * (n+1)

dp_ans[0] = 1
for i in range(1, n+1):
    # 행이 늘어날 때 마다 3가지의 경우를 고려해야함
    
    #1. 이전 dp 에서 아무것도 추가하지 않았을 때
    dp[i][0] = dp_ans[i-1]
    #2. 새로운 행에 왼쪽을 추가하는 경우 => 이전 dp 중 왼쪽아래를 선택한 dp만큼 빼기
    dp[i][1] = dp_ans[i-1] - dp[i-1][1]
    #3. 새로운 행에 오른쪽을 추가하는 경우 => 이전 dp 중 오른쪽아래를 선택한 dp 만큼 빼기
    dp[i][2] = dp_ans[i-1] - dp[i-1][2]
    
    # 1+2+3의 경우를 합쳐서 dp[i]를 정의
    dp_ans[i] = (dp[i][0] + dp[i][1] + dp[i][2]) % 9901

print(dp_ans[n])