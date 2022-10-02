'''
1. 팀원뽑기 = 조합


'''
import sys
input = sys.stdin.readline

def pick_team(ck, s = 1):   # 조합
    if len(tmp) < n//2:
        for i in range(s, n+1 - ck):
            tmp.append(i-1)
            ck -= 1
            pick_team(ck, i+1)
            tmp.pop()
            ck += 1

    else:           # 팀 완성
        team1.append(tmp[:])

n = int(input())
bingo = []
for _ in range(n):
    bingo.append(list(map(int, input().split())))

ck = n//2 -1
team1 = []

# team1 조합
tmp = []
pick_team(ck)

# 시너지 계산
synergy = []
for t in range(len(team1)):
    team1_sy = 0
    for i in range(n//2):
        for k in range(n//2):
            team1_sy += bingo[team1[t][i]][team1[t][k]]
    synergy.append(team1_sy)

result = float('inf')
for i in range(len(synergy)//2):
    if abs(synergy[i] - synergy[-1-i]) < result:
        result = abs(synergy[i] - synergy[-1-i])
        if result == 0:
            break

print(result)