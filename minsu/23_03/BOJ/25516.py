import sys
sys.setrecursionlimit(10**7)

n, k = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

apple = list(map(int, sys.stdin.readline().split()))
result= 0

def check(node, dist):
    global result
    if dist > k:
        return
    result += apple[node]

    for i in graph[node]:
        check(i, dist + 1)

check(0, 0)
print(result)