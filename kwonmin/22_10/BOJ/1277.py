# 발전소 아이디어
# 각 발전소 사이의 거리를 필드에 넣는다.
# 이미 연결되어있는 발전소의 경우 쌍방의 비용을 0으로 한다.
# 다익스트라를 돌린다.

# 발전소의 수와 이어져있는 전선의 수를 준다.
# 발전소의 수+1만큼 (0은안쓰니까) 좌표 필드를 설정해둔다.
# field를 설정하고, 초기값을 INF로 설정한다.
# 좌표 필드에는 각 발전소의 좌표값을 넣는다.
# field도 N+1 x N+1만큼 만들어둔다.
# 각 좌표 간 거리를 계산해서 필드에 거리값을 채운다.
# 이 때, 제한길이를 넘으면 안채워준다.(INF로 냅둠)
# 그런 뒤 이미 이어진 거리의 경우 0으로 수정한다.
# 발전소 visited를 만든다.
# 다익스트라를 돌린다.
# int(거리 x 1000) 출력
import heapq
import sys
input = sys.stdin.readline

INF = 100000000
N, K = map(int,input().split())
lim = float(input())
gens = [[] for _ in range(N+1)]
distance = [INF]*(N+1)
for i in range(1,N+1):
    x, y = map(int,input().split())
    gens[i].append((x,y))

field = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(K):
    aa, bb = map(int,input().split())
    field[aa][bb] = 0
    field[bb][aa] = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            field[i][j] = 0
            continue
        if field[i][j] == INF:
            ax, ay = gens[i][0]
            bx, by = gens[j][0]
            gap = (abs(ax-bx)**2 + abs(ay-by)**2)**0.5
            if gap <= lim:
                field[i][j] = gap
                field[j][i] = gap
            else:
                field[i][j] = INF+1
                field[j][i] = INF+1

def dijkstra(start):
    que = []
    que.append((0,start))
    distance[start] = 0
    while que:
        dis, now = heapq.heappop(que)
        if distance[now] < dis:
            continue
        for i in range(1, N+1):
            cost = dis + field[now][i]
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(que, (cost, i))

dijkstra(1)
print(int(distance[N]*1000))