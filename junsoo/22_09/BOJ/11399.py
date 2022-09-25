'''
5
3 1 4 3 2

1
1 2
1 2 3
1 2 3 3
1 2 3 3 4

'''
import sys
input = sys.stdin.readline

t = int(input())

n = list(map(int, input().split()))

n.sort()

result = 0
for i in range(t):
    result += n[i] * (t - i)

print(result)