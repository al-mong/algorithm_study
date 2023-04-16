import sys
input = sys.stdin.readline

n = int(input())

in_list = []
out_list = []
for i in range(n):
    in_list.append((i, input()))

for i in range(n):
    out = input()
    for j in range(n):
        if in_list[j][1] == out:
            out_list.append(in_list[j][0])
            break

count = 0
for i in range(n):
    for j in range(i+1, n):
        if out_list[j] < out_list[i]:
            count += 1
            break

print(count)