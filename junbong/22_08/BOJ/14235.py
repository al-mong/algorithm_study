import sys, heapq

input = sys.stdin.readline
n = int(input().rstrip())
heap = []

for _ in range(n):
    line = input()
    if line[0] != '0':
        arr = list(map(int, line.split()))
        for i in range(arr[0]):
            heapq.heappush(heap, -arr[i + 1])  # 최대 힙 구조로 만들어주기 위해 - 붙임
    else:
        if heap:
            print(-heapq.heappop(heap))  # 빼낼 때 다시 양수로
        else:
            print(-1)