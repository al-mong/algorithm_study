# 230227
import sys
from collections import defaultdict

input = sys.stdin.readline

cnt_dict = defaultdict(int)

for _ in range(int(input())):
    cnt_dict[int(input())] += 1

key_list = sorted(cnt_dict.keys())
max_have_num, max_have_cnt = 0, 0

for key in key_list:
    if cnt_dict[key] > max_have_cnt:
        max_have_cnt = cnt_dict[key]
        max_have_num = key

print(max_have_num)
