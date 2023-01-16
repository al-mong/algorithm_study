# 세로선 n 가로선 m (m*n) 세로선마다 가로선 위치 개수는 h
# 원하는 사다리 타기를 만들기 위해 추가해야하는 최솟값

import sys
input = sys.stdin.readline

def ladder():
    for i in range(n):
        k = i
        for j in range(h):
            if graph[j][k]:
                k += 1
            elif k> 0 and graph[j][k-1]:
                # 바로 옆에 사다리가 있다면
                k-=1
        if i != k:
            return False
    return True

def dfs(cnt, x, y):
    global value
    if value != -1:
        return
    if cnt == 0:
        if ladder():
            value = cnt
        return
    for i in range(x,h):
        for j in range(n-1):
            if i == x and j == y:
                continue
            if j > 0 and graph[i][j-1]:
                continue
            if graph[i][j] or graph[i][j+1]:
                continue
            graph[i][j] = 1
            dfs(cnt-1,i,j)
            graph[i][j] = 0
        

n,m,h = map(int, input().split())
graph = [[0]*n for _ in range(h)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
value = -1
for cnt in range(4):
    dfs(cnt, 0, -1)
    if value == -1:
        continue
    else:
        break
print(value)

    
