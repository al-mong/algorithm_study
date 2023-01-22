from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

for i in range(n):
    for j in range(i+1, n):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
            B[i], B[j] = B[j], B[i]

dp = [1]
x = [B[0]]

for i in range(1, len(B)):
    if B[i] > x[-1]: # 현재 값이 x 배열의 마지막 값보다 클 경우
        x.append(B[i]) # x 배열에 현재 값을 추가해 주고
        dp.append(dp[-1] + 1) # 증가 부분 수열의 길이를 1 증가시킨다.
    else: # 그렇지 않을 경우
        idx = bisect_left(x, B[i]) # 현재 값이 x 배열의 몇 번째 인덱스에 들어갈 수 있는지를 찾아서
        x[idx] = B[i] # x 배열의 idx 위치에 현재 값을 넣어준다.

print(n-len(x))