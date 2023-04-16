# 230416
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city, houses, chickens = [], [], []
for i in range(N):
    line = list(map(int, input().split()))
    city.append(line)
    for j in range(N):
        if line[j] == 1:
            houses.append([i, j])
        elif line[j] == 2:
            chickens.append([i, j])

result = (N - 1) * 2 * N * 2

for alive_chickens in combinations(chickens, M):
    tmp = 0
    for house in houses:
        chicken_dis = (N - 1) * 2
        for j in range(M):
            chicken_dis = min(chicken_dis, abs(
                house[0] - alive_chickens[j][0]) + abs(house[1] - alive_chickens[j][1]))
        tmp += chicken_dis
    result = min(result, tmp)

print(result)
