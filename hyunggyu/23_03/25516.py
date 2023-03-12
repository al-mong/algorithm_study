import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

from collections import deque

# 0은 루트 n-1까지 정점이 존재 간선 길이는 1 각 정점에는 사과가 있거나 없다. 루트에서 k거리 이하의 경로에 사과만 수확
n, k = map(int, input().split())
tree = [[] for _ in range(n)]
for i in range(n-1):
    p, s = map(int , input().split())
    tree[p].append(s)
visited = [0 for _ in range(n)]
apple = list(map(int, input().split()))
stack = deque([(0,0)])
result = 0
while stack:
    a, b = stack.popleft()
    if b > k: # 경로가 길면
        continue
    result += apple[a] # 사과 더하기
    if visited[a]: # 방문 했던 곳이면 셈하지 않기
        continue
    for i in range(len(tree[a])):
        stack.append((tree[a][i], b+1))
        visited[a] = 1
print(result)   