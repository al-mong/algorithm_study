# 5
# 0
# 2 3 2
# 0
# 0
# 0

import sys, heapq
input = sys.stdin.readline
heap = []
for _ in range(int(input())):                       # n 만큼 반복
    input_list = list(map(int, input().split()))    # 인풋 입력받기
    if len(input_list) == 1:                        # 인풋이 split() 했을 때 길이가 1이면 선물을 줘야함
        if heap:                                    # 힙에 요소가 있으면
            print(-heapq.heappop(heap))             # 맥스를 빼냄
        else:                                       # 힙에 요소가 없으면
            print(-1)                               # -1을 빼냄
        pass
    else:                                           # 인풋이 split() 했을 때 길이가 2 이상이다? => 거점지임
        for i in range(1, input_list[0]+1):         # input[0] 번째 만큼 반복문을 돌아서
            heapq.heappush(heap, -input_list[i])    # input[1] ~ input[a+1] 까지 힙에 요소를 넣음!
                                                    # heapq는 min 우선순위 큐인데
                                                    # push할때 -를 하고 pop을 해서 다시 -를 붙이면 max 우선순위 큐로 쓸 수 있음
            
