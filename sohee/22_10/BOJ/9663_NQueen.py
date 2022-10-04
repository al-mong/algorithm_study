import sys
input = sys.stdin.readline

def f(n, r, i):
    global cnt
    # 대각선부분을 다 확인해야함
    # print(f'p={p} i={i}') 이걸로 i 체크하기
    for s in range(i-1):
        if p[s] + (i-1-s) == p[i-1] or p[s] - (i-1-s) == p[i-1]:
            return
    if i == r:
        cnt += 1
    else:
        for j in range(n):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(n, r, i+1)
                used[j] = 0

N = int(input())
R = N
a = [i for i in range(1, N+1)]
used = [0] * N
p = [0] * R
cnt = 0
f(N, R, 0)
print(cnt)
