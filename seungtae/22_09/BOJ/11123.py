import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    # n x m 행렬을 모두 탐색
    count = 0
    for i in range(n):
        for j in range(m):
            # [i][j]점이 방문한적 없고 현재 위치에 양이 있는경우 BFS 탐색 시작하며 count를 1 올려줌
            if not visited[i][j] and arr[i][j] == '#':
                count += 1
                q = deque([(i, j)])
                visited[i][j] = True
                # 큐가 빌 때 까지(연결된 양을 모두 탐색했을 때 까지) while문 동작
                while q:
                    x, y = q.popleft()
                    # 상하좌우 4칸을 탐색하며 더 갈 수 있으면 큐에 push 및 방문기록 체크
                    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        nx = x + dx
                        ny = y + dy
                        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or arr[nx][ny] != '#':
                            continue
                        q.append((nx, ny))
                        visited[nx][ny] = True
    print(count)
    