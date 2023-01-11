import sys
input = sys.stdin.readline

n = int(input())

adj = {i: [] for i in range(1, n+1)}
adj_count = [0 for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    adj_count[a] += 1
    adj_count[b] += 1


leaf = []
for i in range(1, n+1):
    if adj_count[i] == 1:
        leaf.append(i)

count = 0
while leaf:

    x = leaf.pop()
    for i in adj[x]:
        for nextt in adj[i]:
            adj_count[nextt] -= 1
            adj[nextt].remove(i)
            if adj_count[nextt] == 1:
                leaf.append(nextt)
        count += 1
        adj[i].clear()

print(count)