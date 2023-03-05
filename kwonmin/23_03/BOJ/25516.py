from sys import stdin; input = stdin.readline
import heapq
N, K = map(int,input().split())
nodes = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)

apples = list(map(int,input().split()))
visited = [1] + [0]*(N+1)
res = 0
if apples[0]:
    res += 1
que = [(0,0)]
while que:
    cnt, nd = heapq.heappop(que)
    if cnt >= K:
        break
    for i in nodes[nd]:
        if not visited[i]:
            visited[i] = 1
            if apples[i]:

                res += apples[i]
            heapq.heappush(que, (cnt+1, i))

print(res)