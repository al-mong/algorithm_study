# 220923

import sys

N = int(sys.stdin.readline().rstrip())
times = sorted(map(int, sys.stdin.readline().split()))
print(sum([times[i] * (N - i) for i in range(N)]))
