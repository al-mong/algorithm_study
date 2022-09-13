# 한 번에 한 계단씩 혹은 두 계단씩 오를 수 있음
# 연속된 세 개의 계단을 모두 밟으면 안 됨
# 그래서, 밟으면 연속 두개를 밟게 됨
# 그럼 '어느 계단을 밟지 않을 것인가'가 중요한 문제
# 3연속이 되지 않으려면, 어느 시점을 밟아야 효율적일까?
# 제약 조건 : 마지막 계단은 반드시 밟아야 함
import sys
input = sys.stdin.readline
N = int(input())
nums = [0]+[int(input()) for _ in range(N)]
if N <= 2:
    print(sum(nums))
    exit()
DP = [0] * (N+1)
# 어차피 마지막 계단을 밟아야 하면, 거꾸로 해도 괜찮지않나?
# 뒤집어서 한다기보다는, 뒤에서 시작해서 판별하는걸로
DP[1] = nums[1]
DP[2] = nums[1]+nums[2]
# 연속으로 값 세 개를 더한 게 오지 않도록 설정해야 함
DP[3] = max(nums[1]+nums[3], nums[2]+nums[3])

# 4부터는 조금 달라짐. 234 가 되면 안됨. 즉 124 혹은 134 가 되어야 함
# 12의 경우 DP[2]에 있으니까 124의 경우 (DP[2]+nums[4]), 134의 경우는??? 그냥 셋 더한거랑 비교할까.. DP[1] + nums[3]+nums[4] ?? 이렇게 한번 짜보자
for i in range(4,N+1):
    DP[i] = max(DP[i-2]+nums[i], DP[i-3]+nums[i-1]+nums[i])

print(DP[N])