"""
최소한의 강의실만 사용하여 모든 수업을 가능하게 하기
다른 강의실 배정 처럼 하나의 종료시간을 기준으로
그것보다 빨리 시작하는 것을 없애기
이 문제에서는 강의실 추가하기


"""

# N = int(input())
# case = []
# for i in range(N):
#     case.append(list(map(int, input().split())))
#     case[i].append(0)
#
# case.sort(key=lambda x: x[1])
#
# for i in range(N):
#     for j in range(i+1,N):
#         if case[i][1] <= case[j][0]:
#

#################

import heapq
n = int(input())
end_time = []
class_time = []
for i in range(n):
    class_time.append(list(map(int, input().split())))

class_time.sort()

heapq.heappush(end_time, class_time[0][1])
for i in range(1, n):
    if class_time[i][0] < end_time[0]:
        heapq.heappush(end_time, class_time[i][1])
    else:
        heapq.heappop(end_time)
        heapq.heappush(end_time, class_time[i][1])
print(len(end_time))