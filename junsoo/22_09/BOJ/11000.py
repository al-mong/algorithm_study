'''
3
1 3
2 3
3 5

'''

import sys
input = sys.stdin.readline

n = int(input())

all_list = []
for _ in range(n):
    all_list.append(list(map(int, input().split())))
all_list.sort(key=lambda x: (x[0], -x[1]))

# all_list = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[0], -x[1]))

all = dict()
for i in all_list:      # i = [1, 3]
    if all.get(i[0]):
        all[i[0]].append(i[1])
    else:
        all[i[0]] = [i[1]]

print(all)

result = -1
while True:
    result += 1

    tmp = 0
    for k, v in all.items():
        if k >= tmp:
            if v:
                tmp = v.pop()

    if tmp == 0:
        break

print(result)

