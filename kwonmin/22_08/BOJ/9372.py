from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    que = deque()
    que.append((start))
    visited[start] = 1
    cnt = 0
    while que:
        start = que.popleft()
        for i in range(1,node+1):
            if field[start][i] == 1 and visited[i] == 0:
                que.append(i)
                visited[i] = 1
                cnt += 1
    return cnt
        

# 상근은 여행도 갈수있다. 부럽다...
# 가장 적은 종류의 비행기
#  심지어 이미 방문한 국가를 거쳐 가도 됨
# 어차피 연결된 노드니까
# 그냥 BFS로 탐색해보면 안되나?
T = int(input())
for test_case in range(1,T+1):
    node, veh = map(int,input().split())
    # 노드 수만큼 일단 이중배열 만들기
    field = [[0]*(node+1) for _ in range(node+1)]
    for _ in range(veh):
        x,y = map(int,input().split())
        field[x][y] = 1
        field[y][x] = 1
    visited = [0]*(node+1)
    # 기본적으로 스타트가 1, 도착지가 node 라고 보면 될 것. cnt 도 받자
    print(bfs(1))
