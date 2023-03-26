import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
answer = [0 for i in range(n)]

for i in range(n):
    x = nums[i]
    count = 0
    for j in range(n):
        if answer[j] == 0:
            if x == count:
                answer[j] = i+1
                break
            else:
                count += 1
print(answer)