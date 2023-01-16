# 230115
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    word_list = sorted([input().rstrip() for _ in range(n)])
    for i in range(n - 1):
        word, next_word = word_list[i], word_list[i + 1]
        if len(word) < len(next_word) and word == next_word[: len(word)]:
            print('NO')
            break
    else:
        print('YES')
