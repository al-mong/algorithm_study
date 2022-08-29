# 거점을 선정해서 선물을 충전
# 자신이 들고 있는 가장 가치가 큰 선물을 선물해 줄 것
# 힙큐를 쓰는 문제. heappop
# 0을 만났을 때 힙팝. 선물이 없으면 -1 출력
# 그 이외는 들어오는 선물의 양.

import heapq # 힙큐 선언

N = int(input()) # 받아올 명령어 갯수 (이만큼 반복)
present = [] # 힙큐로 사용할 빈 리스트 선언
for _ in range(N): # N만큼 반복
    cmd, *prs = map(int,input().split()) # 명령어와 나머지를 args 형태로 받아 옴. 0일 경우를 제외하곤 cmd는 필요없음
    if cmd == 0: # cmd가 0일 경우
        if present: # 만약 큐에 값이 있으면
            print(heapq.heappop(present)[1]) # 제일 큰 값을 뽑아냄
        else: # 값이 없으면
            print(-1) # -1을 출력함
    else: # cmd가 0 이 아닐 경우
        for pr in prs: # prs는 *args 형태로 받아왔기 때문에 리스트 형태로 구현되어있음. 값을 하나씩 힙큐에 넣어줌
            heapq.heappush(present, (-pr, pr))

