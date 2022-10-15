'''
랭커 코드

'''
import sys
from itertools import combinations as cb
N = int(sys.stdin.readline()) // 2
M = 2*N
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
allstat = sum(newstat) // 2
mins = 65535
# print(newstat)
# print(list(cb(newstat[:-1], N)))
# print(list(cb(newstat, N)))
# print(newstat[:-1])
for l in cb(newstat[:-1], N):
    mins = min(mins, abs(allstat - sum(l)))
print(mins)