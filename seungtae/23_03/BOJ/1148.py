import sys
from collections import defaultdict
input = sys.stdin.readline

words = []
while True:
    word = input().rstrip()
    if word == '-':
        break
    words.append(word)


alphabet = defaultdict(int)

while True:
    case = input().rstrip()
    if case == '#':
        break

    answer = defaultdict(int)
    case_dit = defaultdict(int)
    for c in case:
        case_dit[c] += 1
        answer[c] = 0
    for word in words:
        word_dic = defaultdict(int)
        for w in word:
            word_dic[w] += 1
        for key, value in word_dic.items():
            if case_dit[key] < value:
                break
        else:
            temp = set(list(word))
            for w in temp:
                answer[w] += 1
    answer = sorted(answer.items(), key=lambda x: x[1])
    max = [answer[0][0]]
    maxV = answer[0][1]
    for i in range(1, len(answer)):
        if answer[i][1] == answer[i-1][1]:
            max.append(answer[i][0])
        else:
            break
    min = [answer[-1][0]]
    minV = answer[-1][1]
    for i in range(1, len(answer)):
        if answer[len(answer)-i-1][1] == answer[len(answer)-i][1]:
            min.append(answer[len(answer)-i-1][0])
        else:
            break
    print("".join(sorted(max)), maxV, "".join(sorted(min)), minV)


