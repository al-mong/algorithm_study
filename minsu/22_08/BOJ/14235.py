import heapq

heap = []
result = []
n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if heap:
            result.append(heapq.heappop(heap)[1])
        else:
            result.append(-1)

    else:
        for i in range(a[0]):
            heapq.heappush(heap, (-a[i+1],a[i+1]))

for i in result:
    print(i)
