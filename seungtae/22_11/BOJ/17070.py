#  브루트포스 재귀로 한칸씩 전부 다 감!

import sys
input = sys.stdin.readline

def f(x, y, state):
    global count
    if x == n-1 and y == n-1:
        count += 1
        return

    # 가로
    if state == 0:
        if y + 1 < n and arr[x][y+1] == 0:
            f(x, y+1, 0)
        if x + 1 < n and y + 1 < n and arr[x][y+1] == 0 and arr[x+1][y] == 0 and arr[x+1][y+1] == 0:
            f(x+1, y+1, 2)

    # 세로
    elif state == 1:
        if x + 1 < n and arr[x+1][y] == 0:
            f(x+1, y, 1)
        if x + 1 < n and y + 1 < n and arr[x][y+1] == 0 and arr[x+1][y] == 0 and arr[x+1][y+1] == 0:
            f(x+1, y+1, 2)

    # 대각선
    else:
        if y + 1 < n and arr[x][y+1] == 0:
            f(x, y+1, 0)
        if x + 1 < n and arr[x+1][y] == 0:
            f(x+1, y, 1)
        if x + 1 < n and y + 1 < n and arr[x][y+1] == 0 and arr[x+1][y] == 0 and arr[x+1][y+1] == 0:
            f(x+1, y+1, 2)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

count = 0
f(0, 1, 0)
print(count)