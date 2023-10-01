import heapq

def solution(A, B):
    answer = 0
    heapq.heapify(A)
    heapq.heapify(B)
    
    while B:
        if heapq.heappop(B) > A[0]:
            heapq.heappop(A)
            answer += 1
    
    return answer