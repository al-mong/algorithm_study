"""
# 무리의 개수를 찾는 문제
#이 있는 곳에 상하좌우로 돌며 붙어있는 것을 한 무리로 인식

"""


import sys
sys.setrecursionlimit(10**6)

def dfs(i,j):
    case[i][j] = '.'    # 지나온곳은 .으로 만들기
    di = [0,1,0,-1]     # → , ↓ , ←, ↑
    dj = [1,0,-1,0]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < H and 0 <= nj < W:
            if case[ni][nj] == '#':
                dfs(ni, nj)


T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())

# 양과 풀의 모습 배열가져오기
    case = []
    for _ in range(H):
        case.append(list(input()))

# 2차원 배열을 돌며 # 무리의 개수 찾기
    cnt = 0
    for i in range(H):
        for j in range(W):
            if case[i][j] == '#':
                dfs(i,j)
                cnt += 1
    print(cnt)