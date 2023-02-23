import sys
input = sys.stdin.readline

from collections import defaultdict

num_count = defaultdict(int)
max_count = 0
max_jiphop = []

n = int(input())
for i in range(n):
    x = int(input())
    num_count[x] += 1
    if num_count[x] > max_count:
        max_count = num_count[x]
        max_jiphop = [x]
    elif num_count[x] == max_count:
        max_jiphop.append(x)

print(min(max_jiphop))