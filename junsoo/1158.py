# 32428kb, 4900ms
from collections import deque                   # deque 모듈

n, k = map(int,input().split())
round = deque()                                 # n용 큐
result = []                                     # 출력용

for i in range(n, 0, -1):                       # n~1까지
    round.append(i)                             # [n, n-1, ... 1]

while round != deque([]):                       # 리스트에 값이 없으면 종료
    for i in range(k):
        if i != k-1:
            round.appendleft(round.pop())       # 리스트 마지막 값을 첫 번째에 넣기
        else:
            result.append(round.pop())          # k 번째는 제거 & 출력용에 넣기


print('<', end='')                              # <
for i in range(len(result)-1):                  # 마지막 전까지 '숫자, ' 조합
    print(f'{result[i]}, ', end='')
print(result[-1], end='')                       # 마지막 숫자만
print('>', end='')                              # >