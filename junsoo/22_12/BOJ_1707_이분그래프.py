import sys
from collections import deque

input = sys.stdin.readline

k = int(input())

for _ in range(k):
    V, E = map(int, input().split())

    graph = {i: set() for i in range(1, V+1)}
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    # print(graph)

    visited = [0 for _ in range(V+1)]
    # bfs
    ck_num = -1 # 그룹 나눌 숫자
    escape = 0  # while문 탈출용

    for s in range(1, V+1): # 모든 점을 다 봐야함
        if visited[s]:
            continue
        que = deque([[s]])  # 시작
        while que:
            ck_num = -ck_num
            qu = que.popleft()  # [1]
            next_que = set()
            for q in qu:        # 1
                if visited[q]:    # 방문했으면
                    if visited[q] != ck_num:
                        print('NO')
                        escape = 1
                        break
                    continue
                visited[q] = ck_num
                next_que |= graph[q]

            if escape:
                break

            if next_que:
                que.append(list(next_que))
        if escape:
            break

    if not escape:
        print('YES')
