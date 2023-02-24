import sys
input = sys.stdin.readline

N = int(input())

nums = dict()
for _ in range(N):
    num = int(input())
    if nums.get(num):
        nums[num] += 1
    else:
        nums[num] = 1

result = 0
maximum = 0
for k, v in nums.items():
    if v > maximum:
        result = k
        maximum = v
    elif v == maximum:
        if result > k:
            result = k

print(result)