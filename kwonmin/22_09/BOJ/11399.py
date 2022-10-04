N = int(input())
nums = list(map(int, input().split()))
nums.sort()
DP = [0] * (N+1)
DP[1] = nums[0]
for i in range(2, N+1):
    DP[i] = DP[i-1] + nums[i-1]

print(sum(DP))