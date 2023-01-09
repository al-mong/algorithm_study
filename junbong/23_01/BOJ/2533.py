import sys; input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def dfs(node):
    for next_node in graph[node]:
        if not visited[next_node - 1]:
            visited[next_node - 1] = 1
            dfs(next_node)
            dp[node - 1][0] += dp[next_node - 1][1]
            dp[node - 1][1] += min(dp[next - 1])


n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 1] for _ in range(n)]
visited = [0 for _ in range(n)]
visited[0] = 1

dfs(1)

print(min(dp[0]))
