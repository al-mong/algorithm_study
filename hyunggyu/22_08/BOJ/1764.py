import sys
a,b = map(int,sys.stdin.readline().split())
listen = dict()
result = []

for i in range(a):
    li_name = sys.stdin.readline().rstrip()
    listen[li_name] = 0        # 딕셔너리에 이름 넣기
for j in range(b):             
    w_name = sys.stdin.readline().rstrip()
    if w_name in listen:       # 딕셔너리의 키에 해당 이름이 있으면
        result.append(w_name)  # 그 이름을 result에 넣기

# 이방식을 사용하면 왜 속도가 빨라질까??
result.sort()
N = len(result)
print(N)
for k in range(N):
    print(result[k])