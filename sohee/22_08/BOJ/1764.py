# 듣보잡. 8월 9일. 실버4
import sys

sys.stdin = open("1764.txt")

N, M = list(map(int, input().split())) # 각각 리스트 만들기
a = []
b = []
for n in range(N):
    a.append(input())
for m in range(M):
    b.append(input())

c = list(set(a) & set(b)) # 원래 for문으로 중복되는거 찾았는데, 시간초과돼서 set로 바꿈
c.sort()
print(len(c))
for idx in c:
    print(idx)


