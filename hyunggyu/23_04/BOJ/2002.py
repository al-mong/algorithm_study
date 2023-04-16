# 대근 ; 차가 터널에 들어가는 순서
# 영식 : 차가 터널에서 나오는 순서
# 차의 수(1~1000)
# 2n+1 줄 
# 차는 6~8 문자 A~Z , 0~9 (중복 x)
import sys
from collections import defaultdict
sys.stdin = open("C:/Users/SSAFY/Desktop/input.txt")
input = sys.stdin.readline
N = int(input())
fast = defaultdict(list)
result = 0
car = list()
for i in range(N):
    op = input().rstrip()
    if car:
        fast[op] = car[:]
    car.append(op)
now = list()
for i in range(N):
    now.append(input().rstrip())
print(car)
print(now)
print(fast)
# 처음에 나보다 빨랐는데 나중에 느린 애를 찾는 것 ; 기준은 자신보다 앞에 있는 차들 기준
# 자기보다 빠른애들을 저장했다가 걔들보다 앞에 있으면 추월한거지
for i in range(N-1,-1,-1):
    tmp = 0
    for j in fast[now[i]]:
        if tmp:
            break
        for k in range(i,N):
            if i == now[k]:
                result += 1
                tmp = 1
                break
print(result)

        
        
        