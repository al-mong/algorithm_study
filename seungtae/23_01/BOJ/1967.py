import sys

sys.setrecursionlimit(10001)
input = sys.stdin.readline

def f(x):
    for y, price in adj[x]:
        if visited[y] == -1:
            visited[y] = visited[x] + price
            f(y)

n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, p = map(int, input().split())
    adj[u].append((v, p))
    adj[v].append((u, p))

visited = [-1 for _ in range(n + 1)]
visited[1] = 0
f(1)        # 여기
maxV, maxIndex = 0, 0
for i in range(1, n+1):
    if visited[i] > maxV:
        maxV = visited[i]
        maxIndex = i
visited = [-1 for _ in range(n + 1)]
visited[maxIndex] = 0
f(maxIndex) # 여기
print(max(visited))