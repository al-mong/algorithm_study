# 1차원으로 순열만 구해도 되는 문제
# 순열의 인덱스를 행으로, 인덱스의 값을 열번호로 생각하면 행과 열이 겹치지 않고 배치 가능
# 그 후 대각선 검증만 하면 완료!

import sys
input = sys.stdin.readline

def f(i, k):
    global count
    for x in range(i-1):                                            # 가지치기
        if p[i-1] == p[x] + (i-1-x) or p[i-1] == p[x] - (i-1-x):    # 대각선이 겹치면 잘라버리기
            return
    if i == k:              # 가지치기에 당하지 않고 i == k 까지 도착하면
        count += 1          # count += 1
    else:
        for j in range(k):          # 순열 구하기
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i+1, k)
                used[j] = 0


N = int(input())
count = 0
a = [i for i in range(N)]
p = [0] * N
used = [0] * N
f(0, N)
print(f'{count}')