import sys
from collections import deque
input = sys.stdin.readline

while True:
    w, h = map(int, input().split())

    if w == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]

    # h x w 행렬을 모두 탐색
    count = 0
    for i in range(h):
        for j in range(w):
            # [i][j]점이 방문한적 없고 현재 위치에 땅이 있는경우 BFS 탐색 시작하며 count를 1 올려줌
            if not visited[i][j] and arr[i][j]:
                count += 1
                q = deque([(i, j)])
                visited[i][j] = True
                # 큐가 빌 때 까지(연결된 땅을 모두 탐색했을 때 까지) while문 동작
                while q:
                    x, y = q.popleft()
                    # [x][y]점의 주변 8칸을 모두 탐색하여 더 갈 수 있으면 큐에 push 및 방문기록 체크
                    for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]:
                        nx = x + dx
                        ny = y + dy
                        if nx < 0 or nx >= h or ny < 0 or ny >= w or visited[nx][ny] or arr[nx][ny] == 0:
                            continue
                        q.append((nx, ny))
                        visited[nx][ny] = True
    print(count)
    