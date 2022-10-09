import sys
input = sys.stdin.readline

n, w  = map(int, input().split())

m = float(input())

dot = dict()
adj = {i: [] for i in range(1, n+1)}

for i in range(1, n+1):                             # 발전소 좌표 위치 dict에 저장
    dot[i] = tuple(map(int, input().split()))       # {1: (0, 0), 2: (0, 1), 3: (1, 1), 4: (2, 1), 5: (2, 2), 6: (3, 2), 7: (3, 3), 8: (4, 1), 9: (4, 3)}

for _ in range(w):                                  # 이어져 있는 전선, 가중치 0으로 저장
    a, b = map(int, input().split())                # {1: [(2, 0)], 2: [(1, 0), (3, 0)], 3: [(2, 0), (4, 0)], 4: [(3, 0)], 5: [], 6: [], 7: [], 8: [], 9: []}
    adj[a].append((b, 0))                           # 정점: [(다음 정점, 비용) 형태
    adj[b].append((a, 0))

                                                    # 두 점 사이의 공식 사용하여 i 번째 점과 i+1 ~ n 번까지의 점의 거리를 모두 계산 후 adj에 저장
                                                    # 단 거리가 m 이상일 시 저장안함
for i in range(1, n):                                                           # { 1: [(2, 0), (2, 1.0), (3, 1.4142135623730951)],
    for j in range(i+1, n+1):                                                   #   2: [(1, 0), (3, 0), (1, 1.0), (3, 1.0), (4, 2.0)],
        d = ((dot[i][0] - dot[j][0])**2 + (dot[i][1] - dot[j][1])**2)**(1/2)    #   3: [(2, 0), (4, 0), (1, 1.4142135623730951), (2, 1.0), (4, 1.0), (5, 1.4142135623730951)],
        if d <= m:                                                              #   4: [(3, 0), (2, 2.0), (3, 1.0), (5, 1.0), (6, 1.4142135623730951), (8, 2.0)],
            adj[i].append((j, d))                                               #      ,,,
            adj[j].append((i, d))                                               #   9: [(6, 1.4142135623730951), (7, 1.0), (8, 2.0)]}


visited = [False for _ in range(n+1)]                   # 방문체크 False로 초기화
dij = [sys.maxsize for _ in range(n+1)]                 # 다익스트라 모든 값 무한으로 설정

visited[1] = True                                       # 1번 발전소 방문체크 True
dij[1] = 0                                              # 1번 dij 비용 0으로 설정
now = 1                                                 # 출발점 1로 설정
while not visited[n]:
    for nextt, price in adj[now]:                       # 1. adj[now]로 이어져 있는 모든 점 비용 갱신
        dij[nextt] = min(dij[nextt], dij[now] + price)

    minV = sys.maxsize
    for i in range(1, n+1):
        if visited[i]:
            continue
        if minV > dij[i]:
            minV = dij[i]
            now = i                                     # 2. 위에서 작업한 비용 갱신 후 방문체크 안된 점 중 가장 작은값을 다음 방문점으로 설정

    visited[now] = True                                 # 3. 다음 방문점 방문체크 후 while문 재동작

print(f'{int(dij[n]*1000)}')