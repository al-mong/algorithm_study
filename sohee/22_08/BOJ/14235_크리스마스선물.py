'''힙큐 문제.실버3
최대값으로 나열을 할거고 힙큐는 원래 최소값으로 정리되게
만들어져 있어서 내용 추가해야함
입력값이 0이거나 몇개의 숫자가 들어가는 거라서
일단은 입력값을 리스트로 받고
0인 경우와 아닌 경우로 나눔
0일 때도 max_heap에 뭐가 있는 경우랑 아닌 경우로 나눔
0이 아닐 때는 리스트 제거해서 추가해야 해서 for문 사용함'''

import heapq

N = int(input())
max_heap = []
result = []

for i in range(N):
    a = list(map(int, input().split()))
    if a == [0]:
        if max_heap:
            result.append(heapq.heappop(max_heap)[1])  # 뭐가 있을 때는 pop 한거의 1번 인덱스를 추가
        else:
            result.append(-1)  # 뭐가 없을 때는 그냥 -1 추가
    else:
        for j in range(1, len(a)):    # 리스트의 첫번째 값은 그냥 개수라서 빼고 1부터 시작쓰~
            heapq.heappush(max_heap, (-a[j], a[j]))  # 최대값부터 저장할거라서 튜플로 앞에 - 붙인거 더해서 추가함
for i in range(len(result)):
    print(result[i])