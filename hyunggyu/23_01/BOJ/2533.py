import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
tree = defaultdict(int)
while True:
    try:
        a, b = map(int, input().split())
        if tree[a] == 0 and tree[b] == 0:
            tree[a] = [b]
            tree[b] = [a]
        elif tree[a] == 0:
            tree[a] = [b]
            tree[b].append(a)
        elif tree[b] == 0:
            tree[a].append(b)
            tree[b] = [a]
        else:
            tree[a].append(b)
            tree[b].append(a)
    except:
        break
# 1은 무조건 존재!
visited = [0]*(n+1)
visited[0] = 1
result = 0
que = [1]
def check():
    global result
    while que:
        a = que.pop()
        if tree[a] == 0:
            continue
        if not visited[a]:
            visited[a] = 1
            result += 1
        b = visited[a] # 1이면 visited[i]에 2를 넣고, 2이면 visited[i]에 1넣기
        for i in tree[a]:
            if not visited[i]:
                visited[i] = (b%2)+1
                if visited[i] == 1:
                    result += 1
                que.append(i)

check()
que.append(range(1,n+1))
check()
print(min(result,n-result))


