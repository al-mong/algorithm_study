import sys


def comb(arr, r):
    result = []
    if r == 1:
        for i in arr:
            result.append([i])
    elif r > 1:
        for i in range(len(arr) - r + 1):
            for j in comb(arr[i + 1:], r - 1):
                result.append([arr[i]] + j)
    return result


input = sys.stdin.readline
N = int(input().rstrip())
board = [list(map(int, input().split())) for _ in range(N)]
arr = [i for i in range(N)]
result = 20000
start_cand = comb(arr, N // 2)
for start in start_cand:
    link = list(set(arr) - set(start))
    start_sum = sum([board[i][j] for i in start for j in start])
    link_sum = sum([board[i][j] for i in link for j in link])
    result = min(abs(start_sum - link_sum), result)
print(result)
