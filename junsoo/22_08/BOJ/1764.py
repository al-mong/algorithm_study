import sys
n, m = map(int, sys.stdin.readline().split())

set_n = set()
set_m = set()

for i in range(n):
    set_n.add(sys.stdin.readline().rstrip())        # .rstrip() 이 없으면 입력 문자열 끝에 \n도 받아버린다 
for i in range(m):
    set_m.add(sys.stdin.readline().rstrip())

result = list(set_n & set_m)
result.sort()

print(len(result))
for i in result:
    print(i)