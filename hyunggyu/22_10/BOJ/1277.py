# 발전소 설치
# 1~n으로 가는 전선이 끊어진걸 이어야 한다.
# 전선의 길이가 m을 초과할수 없다
# 발전소 수 n 남아있는 전선수 w
import heapq
INF = int(1e6)
n, w = map(int, input().split()) # 1000, 10000까지
# m전선 길이
m = float(input()) # 200000까지
# 1~n번 발전소 좌표 x,y
where = []
# 발전소의 위치 0~n-1인덱스에 입력
for k in range(n):
    x,y = map(int, input().split())
    where.append((x,y)) # -100000~100000
# dp를 통해서 최소 거리를 지정
graph = [[] for _ in range(n+1)]

# 이을수 있는 전선 입력
for i in range(w):
    a, b = map(int, input().split())
    graph[a].append((b,0)) # a 에서 b로 가는데 0만큼 소모

for j in range(n): # 전선의 가중치 넣기
    for i in range(n):
        if i == j:
            continue
        d = ((where[j][0] - where[i][0])**2 + (where[j][1] - where[i][1])**2)**(1/2)
        if d <= m: # 전선 길이의 한계까지 되는 곳만 넣기
            graph[j+1].append((i+1,d))
print(graph)
distance = [INF]*(n+1)
def dijkstra(start,end):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance[end]*1000

result = int(dijkstra(1,n))
print(result)