# 8월14일. 실버4. 1026. 보물. 스터디 공통문제. 정렬
# B의 값을 재배열하지 말래서 어떻게 푸는건가 싶었음...
# 재배열하지 말랬지 값 바꾸는 거에 대해서는 별말 없었으니까 0으로 값 다 바꿔버림 ㅋㅋㅋ
# 최대값들 찾아서 새로운 리스트에 넣고 B의 값들은 0으로 바꿔서 품

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = []
for i in range(len(B)):
    max_idx = 0
    for j in range(1, len(B)):
        if B[max_idx] < B[j]:
            max_idx = j
    C.append(B[max_idx])
    B[max_idx] = 0
A.sort()
total = 0
for i in range(len(A)):
    total += A[i] * C[i]
print(total)
