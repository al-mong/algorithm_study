import sys
input = sys.stdin.readline

def f(i, d):
    visited[i] = 1

    if i == 1:
        right(i, d)
    elif i == 4:
        left(i, d)
    else:
        right(i, d)
        left(i, d)

    if d == 1:
        temp = gear[i].pop(7)
        gear[i].insert(0, temp)
    else:
        temp = gear[i].pop(0)
        gear[i].append(temp)

def right(i, d):
    if visited[i + 1] == 0:
        if gear[i][2] != gear[i + 1][6]:
            if d == 1:
                f(i + 1, -1)
            else:
                f(i + 1, 1)

def left(i, d):
    if visited[i - 1] == 0:
        if gear[i][6] != gear[i - 1][2]:
            if d == 1:
                f(i - 1, -1)
            else:
                f(i - 1, 1)


gear = [[]] + [list(map(int, list(input().rstrip()))) for _ in range(4)]

n = int(input())
for _ in range(n):
    visited = [0, 0, 0, 0, 0]
    index, direction = map(int, input().split())
    f(index, direction)