# 220810
# 120ms

'''
처음에는 d와 b를 리스트로 받고
이중 반복문으로 중복 이름 검사
==> 시간초과 뜸

중복 이름 없다는 부분 읽고 세트로 받을까 생각함
세트로 받았으니 교집합
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
d = set(input().rstrip() for _ in range(n))
b = set(input().rstrip() for _ in range(m))

db = list(d & b)

db.sort()

print(len(db))
for name in db:
    sys.stdout.write(name + '\n')
