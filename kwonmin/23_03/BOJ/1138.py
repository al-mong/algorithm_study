from sys import stdin; input = stdin.readline
from collections import defaultdict
# 각 사람은 자기 왼쪽에 자기보다 큰 사람이 몇 명 있는지만 기억함
# 감이 잘 안오긴하네
# 1번부터 N번까지 숫자를 받음.
# can_cnt 를 센다.
# can_cnt 와 맞는 친구를 우선 집어넣는다.


N = int(input())
nums = list(map(int, input().split()))
visited = [0]*N

for i in range(N):
    can_cnt = 0 # 왼쪽에 큰 사람이 몇명이 있는지에 대한 카운터
    for j in range(N):
        if visited[j]:  # 방문했을 경우 그냥 패스
            continue
        if can_cnt == nums[i]: # 들어갈 순번이고, 방문하지 않았으면
            visited[j] = i + 1 # 0부터 시작인 관계로 +1
            break # 이번 순서를 채운 관계로 break
        else: # 들어갈 순번이 아니고 방문하지도 않았을 경우
            can_cnt += 1 

print(*visited)

