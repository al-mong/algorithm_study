# 221219
import sys; input = sys.stdin.readline
from collections import defaultdict, deque


def bfs(s):
    q = deque([s])
    visited[s] = True  # 표시 + 시작점 방문 체크

    while q:
        v = q.popleft()
        for nv in graph[v]:
            if visited[nv] == -1:  # 인접 정점에 방문하지 않았으면
                visited[nv] = not visited[v]  # 인접 정점에 현재 정점과 반대 표시 + 방문 체크
                q.append(nv)
            elif visited[nv] == visited[v]:  # 인접 정점이 방문했던 곳인데, 현재 정점과 같은 표시라면
                return False  # 이분 그래프가 될 수 없음

    return True


for _ in range(int(input().rstrip())):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [-1] * (V + 1)  # -1: 미방문
    for i in range(1, V + 1):
        if visited[i] == -1:
            if not bfs(i):
                print("NO")
                break
    else:
        print("YES")
