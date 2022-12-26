N = int(input())
DP = [0]*(N+1)
# 홀수일 때는 못채움
if not N % 2:
    print(0)
else:
    DP[2] = 3

# DP[4] = 11인데
# 숫자 세다가 포기