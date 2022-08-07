# 220805
import sys
from collections import deque

'''
1. 큐 문제인 이유
큐: 선입선출-FIFO(First In First Out)
원을 따라 계속해서 순회하면서 매 k번째마다 뽑아내는 방식은
큐에서 매 k번째 순서가 아니면 뽑아내서 다시 큐에 넣고
k번째는 뽑아서 결과에 저장하는 방식과 같다.
따라서 큐를 사용하면 편하게 해결할 수 있다.

2. 풀이
q에 원소가 남아있는 동안 1번의 방식대로 진행.
'''

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
