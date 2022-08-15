# 220811
# 72ms

'''
k가 문제에서 주어진 0 ~ n - 1일 때
a의 k번째(인덱스) 최소값, b의 k번째 최대값끼리 곱해서 합하면
원소간 곱셈의 합 S가 최소이므로
a는 정렬
b는 index로 최대값을 찾아 pop으로 뽑아내면서 계산
'''
import sys

input = sys.stdin.readline
N = int(input().rstrip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0

A.sort()

for i in range(N):
    a = A[i]
    b = B.pop(B.index(max(B)))
    result += a * b

print(result)
