from sys import stdin; input = stdin.readline
from collections import defaultdict, deque

def BFS(start):
    que = deque()
    que.append(start)
    visited[start] = 1
    while que:
        x = que.popleft()
        
        for next in nodes[x]:
            if visited[next]:
                if visited[next] == visited[x]:
                    return 'NO'
                else:
                    continue
            visited[next] = visited[x]*(-1)
            que.append(next)
    return 'YES'
            

T = int(input())
for _ in range(T):
    V, E = map(int,input().split()) # V는 정점의 개수, E는 간선의 개수
    # 다른 정점과 이어지지 않은 정점의 경우에는, 따로 생각할 필요가 없음
    # 그 자체로도 이분 그래프의 조건을 충족하기 때문
    nodes = defaultdict(list)
    visited = [0]*(V+1)
    res = ''
    for _ in range(E):
        s, e = map(int,input().split())
        nodes[s].append(e)
        nodes[e].append(s)
    
    for i in range(1,V+1): # 간선 돌면서 확인하기. 모든 노드가 이어져 있지 않을 경우를 생각해서 전부 탐색
        if not visited[i]:
            res = BFS(i)
        if res == 'NO':
            break
    print(res)
    