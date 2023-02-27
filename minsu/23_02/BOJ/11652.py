N = int(input())

num = {}
total = 0
cnt_num = 0
for _ in range(N):
    a = int(input())
    if a in num:
        num[a] += 1
    else:
        num[a] = 1

for i in num.keys():
    if num[i] > total:
        total = num[i]
        cnt_num = i
    elif num[i] == total and cnt_num>i:
        cnt_num = i
print(cnt_num)