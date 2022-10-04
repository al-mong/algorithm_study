'''
1. 팀원뽑기 = 조합
2. 조합 리스트의 반대쪽은 반대 조합

'''
import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
bingo = []
for _ in range(n):
    bingo.append(list(map(int, input().split())))

man = []
for i in range(n):
    man.append(i)

# team1 조합
combi = list(combinations(man, n//2))
print(combi)
# 시너지 계산
synergy = []
for t in combi:
    team1_sy = 0
    for i in t:
        for k in t:
            team1_sy += bingo[i][k]
    synergy.append(team1_sy)

result = float('inf')
for i in range(len(synergy)//2):
    if abs(synergy[i] - synergy[-1-i]) < result:
        result = abs(synergy[i] - synergy[-1-i])
        if result == 0:
            break

print(result)