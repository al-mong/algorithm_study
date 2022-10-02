# 221002

def backtrack(i):
    global cnt
    if i == N:
        cnt += 1
    else:
        N_copy = N
        if N % 2 == 0 and i == 0:
            N_copy //= 2
        for j in range(i, N_copy):
            if col_check[p[j]] or right_top_check[i + p[j]] or left_top_check[i + N - 1 - p[j]]:
                continue
            p[i], p[j] = p[j], p[i]
            col_check[p[i]] = 1
            right_top_check[i + p[i]] = 1
            left_top_check[i + N - 1 - p[i]] = 1
            backtrack(i + 1)
            col_check[p[i]] = 0
            right_top_check[i + p[i]] = 0
            left_top_check[i + N - 1 - p[i]] = 0 
            p[i], p[j] = p[j], p[i]


N = int(input())
p = [i for i in range(N)]
col_check = [0] * N
right_top_check = [0] * (2 * N - 1)
left_top_check = [0] * (2 * N - 1)
cnt = 0
backtrack(0)
if N % 2 == 0:
    cnt *= 2
print(cnt)