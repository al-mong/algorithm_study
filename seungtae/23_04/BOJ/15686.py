import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i, j))


ans = 1000000
for s_chicken in combinations(chicken, m):
    minDSum = 0
    flag = False
    for i in range(n):
        if flag:
            break
        for j in range(n):
            if arr[i][j] == 1:
                minD = []
                for x, y in s_chicken:
                    minD.append(abs(i-x) + abs(j-y))
                minDSum += min(minD)
                if minDSum > ans:
                    flag = True
                    break
    else:
        if ans > minDSum:
            ans = minDSum
print(ans)