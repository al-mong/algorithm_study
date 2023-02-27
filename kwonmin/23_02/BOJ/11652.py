from sys import stdin; input=stdin.readline
N = int(input())

nums_dict = {}
for i in range(N):
    N = int(input())
    if N in nums_dict:
        nums_dict[N] += 1
    else:
        nums_dict[N] = 1

dict_list = list(nums_dict.items())
dict_list.sort(key=lambda x:(-x[1], x[0]))
print(dict_list[0][0])