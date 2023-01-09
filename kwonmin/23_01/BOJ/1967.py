from sys import stdin; input=stdin.readline
from collections import defaultdict
from itertools import combinations

# 약간 너무 어렵게 생각했을수도?

def DFS(x, level):
    visited[x] = 1
    depth[x] = level
    if x not in sons:
        comb_list.append(x)
        return
    for i in sons[x]:
        if visited[i]:
            continue
        DFS(i, level+1)


N = int(input())

sons = defaultdict(list)
parent = defaultdict(list)
depth = [0]*(N+1)
visited = [0] * (N+1)
max_val = 0
comb_list = []

for _ in range(N-1):
    pa, son, val = map(int,input().split())
    sons[pa].append(son)
    parent[son].append((pa, val))

DFS(1, 1)

if len(sons[1]) == 1:
    comb_list.append(1)

for a, b in combinations(comb_list, 2):
    tot = 0
    if depth[a] < depth[b]:
        a, b = b, a
    
    while depth[a] != depth[b]:
        q, w = parent[a][0]
        a = q
        tot += w

    while a != b:
        q, w = parent[a][0]
        e, r = parent[b][0]

        a, b = q, e
        tot = tot + w + r
    
    max_val = max(max_val, tot)

print(max_val)