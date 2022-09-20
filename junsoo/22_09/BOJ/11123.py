'''
재귀 깊이 제한을 어디까지 해제하는 것이 좋은지 정하는 방법은?

'''

import sys
sys.setrecursionlimit(100000)

def check(i, k):
    if total[i][k] == '#':
        total[i][k] = '.'
        for d in range(4):
            check(i+dy[d], k+dx[d])


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

t = int(input())

for t in range(t):
    h, w = map(int, sys.stdin.readline().split())
    total = [['.' for i in range(w+2)]]
    for i in range(h):
        sheep = ['.'] + list(map(str, sys.stdin.readline().strip())) + ['.']
        total.append(sheep)
    total += [['.' for i in range(w + 2)]]

    result = 0
    for i in range(1, h+1):
        for k in range(1, w+1):
            if total[i][k] == '#':
                result += 1
                check(i, k)
    print(result)