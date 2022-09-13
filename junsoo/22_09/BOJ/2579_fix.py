import sys
input = sys.stdin.readline

def stair(n):
    if n == 1:
        result[n] = num[n]
    elif n == 2:
        result[n] = num[n] + result[n - 1]
    elif n == 3:
        result[n] = max(result[n - 1], num[n] + result[n - 2])
    else:
        result[n] = max(num[n] + num[n - 1] + result[n - 3], num[n] + result[n - 2])

n = int(input())

num = [0 for _ in range(n + 1)]
result = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    num[-i] = int(input())

for i in range(1, n + 1):
    stair(i)

print(max(result))
