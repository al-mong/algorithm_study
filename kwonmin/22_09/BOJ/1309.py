N = int(input())
DP = [0]*(N+5)
DP[1] = 3
DP[2] = 7
DP[3] = 17
DP[4] = 41
if N < 5:
    print(DP[N])
    exit()

for i in range(5,N+1):
    DP[i] = (DP[i-2] + DP[i-1]*2)%9901

print(DP[N])
