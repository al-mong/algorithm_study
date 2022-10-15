'''
발전소간 거리 표를 제작하여 다익스트라 사용

'''

from collections import deque
import sys

# 길이 측정
def length(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

input = sys.stdin.readline

# 발전소 개수, 연결된 전선의 수
n, w = map(int, input().split())
# 전선 제한 길이
m = float(input())

# 발전소 위치
power = [list(map(int, input().split())) for _ in range(n)]
# 연결된 발전소
link = [list(map(int, input().split())) for _ in range(w)]
# 발전소 거리표
ground = [[length(power[i], power[k]) for i in range(n)]for k in range(n)]
for i in link:
    ground[i[0]-1][i[1]-1] = ground[i[1]-1][i[0]-1] = 0
    # 발전소 번호 - 1 = 인덱스 번호

# 방문 확인
visited = [float('inf') for _ in range(n)]
visited[0] = 0

que = deque()
que.append(0)  # 1번 발전소 번호

while que:
    q = que.popleft()
    for i in range(n):
        # 제한 값보다 작을 때
        if ground[q][i] <= m:
            # 기존 값보다        새 값이 작으면
            if visited[i] > visited[q] + ground[q][i]:
                visited[i] = visited[q] + ground[q][i]
                que.append(i)

print(int(visited[-1]*1000))