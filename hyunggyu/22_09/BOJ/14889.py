# 사람 수 n = even
# 1~n까지 배정해서 팀의 능력치를 더한게 s12, s21 된게 그 팀의 능력치
# 게임의 재미를 위해 능력치 차이를 최소로 하려고 한다.
import sys
n = int(input())
ability = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
# # 아래 삼각형에 위 삼각형의 값의 대칭값을 더해준다.
# 1,2,3 팀이면 4,5,6 팀
# j > i인 조건에서만 더할것
# 팀을 먼저 나누자
def team(n,m,j):
    if n==m:
        a.append(chosen[:])
        return
    for i in range(j,len(arr)):
        chosen[n] = arr[i]
        team(n+1,m,i+1)
m = n//2
arr = list(range(n))
chosen = [-1]*m
a = []
team(0,m,0)
result = 10000
for k in range(len(a)//2):
    cnt = 0
    for i in a[k]: # [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]] 서로 대칭
        for j in a[k]:
            if i == j:
                continue
            else:
                cnt += ability[j][i]
    for i in a[-k-1]:
        for j in a[-k-1]:
            if i == j:
                continue
            else:
                cnt -= ability[j][i]
    if abs(cnt) < result:
        result = abs(cnt)
print(result)