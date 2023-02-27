# 가장 많은 카드를 고르시오 그중 가장 작은값으로
import sys
input = sys.stdin.readline
from collections import defaultdict


dic = defaultdict(int)
n = int(input())
total = 0
m = 0
for i in range(n):
    a = int(input())
    dic[a] += 1
    if dic[a] > total:
        m = a
        total = dic[a]
    elif dic[a] == total:
        if m > a:
            m = a
print(m)

    