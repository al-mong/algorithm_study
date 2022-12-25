n = int(input())

# 단어마다 나온 횟수 + 자릿수 체크
decided = {chr(i): 0 for i in range(65, 91)}
for _ in range(n):
    word = input()
    for i in range(len(word)):
        decided[word[i]] += 10**(len(word)-1-i)

# 한번이상 나온 단어를 새로운 곳에 저장후 내림차순 정렬
count_num = []
for i in range(65, 91):
    if decided[chr(i)] != 0:
        count_num.append(decided[chr(i)])
count_num.sort(reverse=True)

# 가장 큰 값이 할당된 곳부터 9~0 을 할당
count = 9
total = 0
for i in range(len(count_num)):
    total += count_num[i] * count
    count -= 1
print(total)