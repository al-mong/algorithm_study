#이건 왜 틀리지??

# from collections import deque
# def solution(A, B):
#     answer = 0
#     A.sort(reverse=True)
#     B.sort(reverse=True)
#     B = deque(B)
#     # print(A,B)
#     for i in range(len(A)):
#         b = B.popleft()
#         if A[i] <= b:
#             answer += 1
#         else:
#             B.appendleft(b)
#     return answer

# 정답코드
from collections import deque
def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    A = deque(A)
    B = deque(B)
    while len(A) != 0:
        a = A.popleft()
        b = B.popleft()
        if a <b:
            answer += 1
        else:
            B.appendleft(b)
    return answer

print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))