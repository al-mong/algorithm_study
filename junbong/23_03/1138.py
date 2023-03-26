# 230323
import sys
input = sys.stdin.readline

N = int(input())
taller = list(map(int, input().split()))
result = [N]

for i in range(N - 1, 0, -1):
    cnt = 0

    while cnt < taller[i - 1]:
        if result[cnt] > i:
            cnt += 1

    result = result[:cnt] + [i] + result[cnt:]

print(*result)
