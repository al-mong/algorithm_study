# 220805
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())  # 입력이 한 줄에 끝나므로 rstrip() 필요 없는 듯
q = deque(list(range(1, n + 1)))  # 1 ~ n
result = deque()
cnt = 1

while q:  # q에 원소가 남아있는 동안 반복
    for _ in range(k - 1):  # k - 1번 동안 큐에서 빼서 다시 넣고
        q.append(q.popleft())
    result.append(q.popleft())  # 매 k번째 것만 result에 저장

print('<' + str(list(result)).lstrip('[').rstrip(']') + '>')
