import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(cur, d):
    global count
    visited[cur] = 1
    if isApple[cur]:
        count += 1
    if d == k:
        return
    for _next in adj[cur]:
        if not visited[_next]:
            dfs(_next, d+1)

n, k = map(int, input().split())
adj = {i:[] for i in range(n)}
visited = [0 for i in range(n)]

for i in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

isApple = list(map(int, input().split()))
count = 0
dfs(0, 0)
print(count)
