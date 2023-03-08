from sys import stdin; input = stdin.readline
from collections import deque

# 아이디어 먼저
# 요세푸스 문제 비슷하게 큐를 로테이션 시키는 형태
# max의 값과 인덱스를 뽑는다 -> 해당 인덱스만큼 로테이션 -> pop
# 이렇게 하면, 시간복잡도가 너무 커질 수도 있음. max가 전체 순회이기 때문


T = int(input())

for _ in range(T):
    N, S = map(int,input().split())
    nums = list(map(int,input().split()))
    rst = deque()
    for i in range(N):
        if i == S:
            rst.append((nums[i], 1))
        else:
            rst.append((nums[i], 0))
    now = max(rst)[0]
    cnt = 0
    flag = 0
    while not flag:
        if rst[0][0] == now:
            if rst[0][1]:
                flag = 1
            rst.popleft()
            cnt += 1
            if rst:
                now = max(rst)[0]
        else:
            rst.rotate(-1)
    print(cnt)

# 결과 : 실버라서 문제가 없었다