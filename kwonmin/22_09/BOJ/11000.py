import sys
import heapq
input = sys.stdin.readline

N = int(input())
start_list = []
end_list = []
for _ in range(N):
    stt, end = map(int,input().split())
    start_list.append(stt)
    end_list.append(end)
heapq.heapify(start_list)
heapq.heapify(end_list)
max_len = 0
que = []
while start_list:
    a = start_list[0]
    b = end_list[0]
    
    if a < b:
        que.append(heapq.heappop(start_list))
        if len(que) > max_len:
            max_len = len(que)
    else:
        heapq.heappop(end_list)
        que.pop()

print(max_len)