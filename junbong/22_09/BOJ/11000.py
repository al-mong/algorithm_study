# 220925

# 힙큐 안쓴 풀이 ===============================================

'''
힙큐 사용했을 때와 같은 기능을 하는 코드이지만
정렬 단계에서 많은 시간을 잡아먹기 때문에
PyPy3로 돌려도 86 % 에서 시간 초과가 남
'''

'''
import sys

input = sys.stdin.readline
N = int(input().rstrip())
lec = sorted((tuple(map(int, input().split())) for _ in range(N)))
room = [lec[0][1]]

for i in range(1, N):
    if lec[i][0] >= room[0]:
        room[0] = lec[i][1]
        room.sort()
    else:
        room.append(lec[i][1])
        room.sort()

print(len(room))
'''

# 힙큐 사용 ======================================================

'''
정렬 단계에서 많은 시간을 아낄 수 있음
=> 힙큐 사용 이유
'''

import sys
import heapq

input = sys.stdin.readline
N = int(input().rstrip())
lec = sorted((tuple(map(int, input().split())) for _ in range(N)))
room = [lec[0][1]]

for i in range(1, N):
    if lec[i][0] >= room[0]:
        heapq.heappop(room)
        heapq.heappush(room, lec[i][1])
    else:
        heapq.heappush(room, lec[i][1])

print(len(room))
