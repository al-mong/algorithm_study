# 실버3

N = int(input())
stairs = [0]  # 계단 value 입력받기
for i in range(N):
    stairs.append(int(input()))

dp = [0] * (N+1) # 누적최대값 적을 리스트 만들어놓기

# N 이 1,2,3 일 때는 최대값 그대로 출력하면 됨
# N 이 3일 경우에는 1,3 더하거나 2,3 더함 
if N == 1:
    print(stairs[1])
elif N == 2:
    print(stairs[1] + stairs[2])
elif N == 3:
    print(max(stairs[1] + stairs[3], stairs[2] + stairs[3]))
# N 이 1,2,3 이 아닐 경우에는, 일단 1,2,3 누적 최대값을 채워놔주기
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    # 4번째 계단부터는 2가지의 경우를 생각해야함
    # 바로 아래층에서 올라왔을 때는 전전칸이 i-3 번째가 되는거임, 그래서 i-3 까지의 최대값이랑 i-1번째의 staris 값 더한거와
    # 전전칸에서, 즉 i-2 칸에서의 누적최대값을 비교해서 max 인거를 추려내야함
    for i in range(4, N+1):
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])
    print(dp[N])
