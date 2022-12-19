import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)          # 재귀 한계 설정 늘려주기
input = sys.stdin.readline

def dfs(u, cur, next):                  # 현재 정점, 현재 정점의 색, 다음 정점의 색
    global flag
    for w in adj[u]:                    # 현재랑 이어져있는 다음 정점 모두 탐색
        if visited[w] == -1:            # 아직 방문 안했으면
            visited[w] = next               # 현재색과 반대되는 색으로 방문체크 후
            dfs(w, next, cur)               # 계속 dfs 실행
        elif visited[w] == cur:         # 이미 다음정점이 현재정점이랑 색이 같으면
            flag = False                    # flag 세우고 종료시키기
            return

k = int(input())

for tc in range(k):
    v, e = map(int, input().split())
    adj = defaultdict(list)
    for _ in range(e):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [-1 for _ in range(v+1)]
    flag = True

    for i in range(1, v+1):             # 모든 정점에 대해 탐색
        if visited[i] == -1:            # 방문안한 점을 찾으면
            visited[i] = 0              # 현재 0, 다음 1로 설정하고
            dfs(i, 0, 1)                # dfs 시작

    if flag:                # 모든 정점 방문 완료 후 flag가 False로 안바뀌었으면
        print("YES")            # 성공
    else:                   # 바뀌었으면
        print("NO")             # 실패

