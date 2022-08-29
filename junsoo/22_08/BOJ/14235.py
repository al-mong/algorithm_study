import sys

n = int(sys.stdin.readline())

a = []
for i in range(n):
    x, *b = list(map(int, sys.stdin.readline().split()))

    if x == 0:
        if a == []:
            print(-1)
        else:
            print(max(a))
            a.remove(max(a))
    else:
        a = a + b
