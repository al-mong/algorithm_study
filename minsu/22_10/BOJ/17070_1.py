import sys

n = int(sys.stdin.readline())
case = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

garo = 0  # 가로
sero = 1 # 세로
dae = 2 # 대각
cnt = 0

def dfs(i, j, t): #
    global cnt
    if (i, j) == (n-1,n-1):
        cnt += 1
        return

# 가로 파이프 깔기
# 이전 파이프가 가로, 대각일 때
    if t == garo or t == dae:
        if j+1 < n and case[i][j+1] == 0 :  # 다음 파이프가 벽을 안 벗어나고, 벽이 없을 떄
            dfs(i, j+1, garo)

# 세로 파이프 깔기
#이전 파이프가 세로, 대각일 때
    if t == sero or t == dae:
        if i +1 <n and case[i+1][j] ==0: # 다음 파이프가 벽을 안 벗어나고, 벽이 없을 떄
            dfs(i+1, j, sero)

# 대각선 파이프 깔기
    if i+1<n and j+1 < n :
        # 대각선은 오른쪽, 대각, 아래가 다 빈칸이어야 함
        if case[i+1][j] == 0 and case[i][j+1] == 0 and case[i+1][j+1] == 0:
            dfs(i+1, j+1, dae)

dfs(0, 1, garo)
print(cnt) 