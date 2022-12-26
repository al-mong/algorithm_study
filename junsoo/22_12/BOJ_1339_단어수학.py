n = int(input())

total = [[] for _ in range(8)]
for _ in range(n):
    word = input()
    len_word = len(word)
    for i in range(len_word - 1, -1, -1):
        total[len_word-i-1].append(word[i])
# print('total', total)

cal = dict()
abcd = 0
for i in range(8):
    for spell in total[i]:
        if cal.get(spell):
            cal[spell] += 10 ** i
        else:
            cal[spell] = 10 ** i
            abcd += 1
# print('cal', cal)

value = dict()
ck = 9
cal_copy = cal.copy()
for _ in range(abcd):
    maximum = ['', 0]
    for k, v in cal_copy.items():
        if maximum[1] < v:
            maximum = [k, v]
    value[maximum[0]] = ck
    ck -= 1
    del cal_copy[maximum[0]]
# print('value', value)

result = 0
for k, v in value.items():
    result += v * cal[k]
print(result)