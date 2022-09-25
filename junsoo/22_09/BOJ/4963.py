import sys
sys.setrecursionlimit(100000)

def check(i, k):
    if mymap[i][k] == 1:
        mymap[i][k] = 0
        for d in range(8):
            check(i+dy[d], k+dx[d])

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    mymap = [[0 for i in range(w + 2)]]
    for i in range(h):
        a = [0] + list(map(int, sys.stdin.readline().split())) + [0]
        mymap.append(a)
    mymap += [[0 for i in range(w + 2)]]

    result = 0
    for i in range(1, h + 1):
        for k in range(1, w + 1):
            if mymap[i][k] == 1:
                result += 1
                check(i, k)

    print(result)