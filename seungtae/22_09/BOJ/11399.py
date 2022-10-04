import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
people.sort()

nujuckhap = [0] * (n+1)
for i in range(1, n+1):
    nujuckhap[i] = nujuckhap[i-1] + people[i-1]     # 누적합 계산

print(sum(nujuckhap))   # 누적합 다 더하기