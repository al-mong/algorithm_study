# 230108

'''
(자식 노드의 가중치 누적합 리스트 중에 가장 큰 값 + 부모 노드로 가기 위한 가중치)를
부모 노드의 가중치 누적합 리스트에 append 한다.
이후 모든 노드들을 탐색하며 가중치 누적합 리스트 중 상위 2개(1개일 수도 있음)의 합이
가장 큰 값이 최대의 지름이 된다.
'''

import sys, heapq; input = sys.stdin.readline
from collections import defaultdict, deque


# 가중치 누적합 완성 함수
def bfs(leafs):
    q = deque(leafs)
    visited = [0 for _ in range(n + 1)]
    
    while q:
        node = q.popleft()
        if node == 1:
            continue
        parent = board[node][0]

        # 자식 노드의 가중치 누적합 리스트 중에 가장 큰 값 + 부모 노드로 가기 위한 가중치를
        # 부모 노드의 가중치 누족합 리스트에 append
        heapq.heappush(cumul_weights[parent], cumul_weights[node][0] - board[node][1])

        if not visited[parent]:  # 이미 방문했으면 큐에는 추가하지 않음
            q.append(parent)
            visited[parent] = 1


n = int(input())
if n == 1:
    print(0)
    exit()
board = defaultdict(list)
level = [0] * (n + 1)  # 레벨이 높은 노드가 먼저 큐에 들어가도록
cumul_weights = defaultdict(list)  # 가중치 누적합 저장
nodes = {i + 1 for i in range(n)}  # 전체 노드
not_leafs = set()  # 리프 노드가 아닌 것들
result = 0

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    board[b].append(a)
    board[b].append(w)
    level[b] = level[a] + 1  # 자식의 레벨이 부모보다 한 단계 높도록
    not_leafs.add(a)

leafs = sorted(list(nodes - not_leafs), key=lambda x: level[x], reverse=True)  # 리프 노드, 레벨이 높은 리프 노드가 앞에 오도록 정렬

for leaf in leafs:
    cumul_weights[leaf].append(0)  # 누적 합 초기화

bfs(leafs)

# 완전 이진 트리가 아니고, 지름을 계산하는 것이므로 1개 또는 최대 2개까지만 계산
for weight in cumul_weights.values():
    cnt = 0
    tmp = 0
    while weight and cnt <= 1:
        tmp += -heapq.heappop(weight)
        cnt += 1
    result = max(tmp, result)

print(result)
