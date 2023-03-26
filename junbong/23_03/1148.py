# 230326
from collections import defaultdict
import sys
input = sys.stdin.readline

word_dicts = []
while True:
    word = input().rstrip()
    if word != '-':
        word_dict = defaultdict(int)
        for char in word:
            word_dict[char] += 1
        word_dicts.append(word_dict)
    else:
        break

while True:
    board = input().rstrip()

    if board == '#':
        break

    board_dict = defaultdict(int)
    for char in board:
        board_dict[char] += 1

    cnt_dict = {key: 0 for key in set(board_dict.keys())}

    for word_dict in word_dicts:
        for key, value in word_dict.items():
            if value > board_dict[key]:
                break
        else:
            for key in set(word_dict.keys()):
                cnt_dict[key] += 1

    min_cnt, max_cnt = min(cnt_dict.values()), max(cnt_dict.values())
    min_chars, max_chars = [], []
    for char, cnt in cnt_dict.items():
        if cnt == min_cnt:
            min_chars.append(char)
        if cnt == max_cnt:
            max_chars.append(char)

    print(''.join(sorted(min_chars)), min_cnt,
          ''.join(sorted(max_chars)), max_cnt)
