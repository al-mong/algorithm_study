'''
3
1 3
2 3
3 5

5
1 3
2 3
3 5
3 8
4 5

한 번의 순회로 답을 제출할 수 있어야 한다.

'''

import sys
import heapq

input = sys.stdin.readline

n = int(input())

all_list = []
for _ in range(n):
    all_list.append(list(map(int, input().split())))
all_list.sort(key=lambda x: (x[0], x[1]))

# all_list = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[0], x[1]))

h = []
for i, v in enumerate(all_list):  # v = [1 3]
    if i == 0:
        heapq.heappush(h, v[1])
    else:
        if v[0] < h[0]:
            heapq.heappush(h, v[1])
        else:
            heapq.heappushpop(h, v[1])

print(len(h))