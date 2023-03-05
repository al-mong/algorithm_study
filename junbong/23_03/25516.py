# 230305
from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs():
    global result, k
    q = deque([0])
    while q:
        node = q.popleft()
        if level[node] > k:
            break
        if apple[node]:
            result += 1
        for next_node in tree[node]:
            q.append(next_node)
            level[next_node] = level[node] + 1


n, k = map(int, input().split())
tree = defaultdict(list)
for _ in range(n - 1):
    p, c = map(int, input().split())
    tree[p].append(c)
apple = list(map(int, input().split()))
level = [0] * n
result = 0

bfs()

print(result)
