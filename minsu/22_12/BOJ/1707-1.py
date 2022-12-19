from collections import deque
import sys

# 기준점에서 연결된 곳이 다른 번호이면 이분 그래프 만족
def bfs(case, start):
    q = deque()
    q.append(start)
    if visited[start] == 0:
        visited[start] = 1
    while q:
        v = q.popleft()
        for i in case[v]:
            if visited[i] == 0:         # 처음 가는 곳
                q.append(i)
                if visited[v] == 1:     # 기준점과 다른 번호를 준다
                    visited[i] = 2
                else:
                    visited[i] = 1

            elif visited[i] == 1:       # 가려는 곳이 1로 갔던 곳
                if visited[v] == 1:     # 기준점이 1이면 이분 그래프 만족 x
                    return False

            elif visited[i] == 2:       # 가려는 곳이 2로 갔던 곳
                if visited[v] == 2:     # 기준점이 2이면 이분 그래프 만족 x
                    flag = 1
                    return False
    return True

K = int(sys.stdin.readline())
for i in range(K):
    V, E = map(int, input().split())
    case = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    # 그래프 만들기
    for j in range(E):
        a, b = map(int, input().split())
        case[a].append(b)
        case[b].append(a)

    # 모든 점에서 bfs 시작
    # 만약 이분그래프를 만족못하면 바로 탈출
    for k in range(1, V+1):
        if not bfs(case,k):
            print('NO')
            break
    else:
        print('YES')
