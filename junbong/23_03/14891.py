# 230319
from collections import deque
import sys
input = sys.stdin.readline


def rotate(q: deque, dr):
    if dr == 1:
        q.appendleft(q.pop())
    else:
        q.append(q.popleft())


def solution(c_num, dr):
    if visited[c_num]:
        return

    visited[c_num] = 1

    three, nine = cogwheels[c_num][2], cogwheels[c_num][6]

    rotate(cogwheels[c_num], dr)

    left, right = c_num - 1, c_num + 1

    if left >= 0 and cogwheels[left][2] != nine:
        solution(left, dr * -1)

    if right < 4 and cogwheels[right][6] != three:
        solution(right, dr * -1)


cogwheels = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
K = int(input())
rotate_plan = [tuple(map(int, input().split())) for _ in range(K)]

for c_num, dr in rotate_plan:
    visited = [0, 0, 0, 0]
    solution(c_num - 1, dr)

result = 0
weight = 1
for cogwheel in cogwheels:
    if cogwheel[0] == 1:
        result += weight
    weight *= 2

print(result)
