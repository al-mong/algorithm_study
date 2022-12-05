def solution(new_id):
    # 1단계
    word = []
    for i in range(len(new_id)):
        word.append(new_id[i])
        if 65 <= ord(word[i]) <= 90:
            word[i] = chr(ord(word[i]) + 32)

    # 2단계
    new_word = []
    for j in range(len(word)):
        if 97 <= ord(word[j]) <= 122 or word[j].isdigit() or word[j] == '-' or word[j] == '_' or word[j] == '.':
            new_word.append(word[j])

    # 3단계
    n = 0
    while True:
        if n == len(new_word) - 1:
            break

        if new_word[n] == '.' and new_word[n+1] == '.':
            del new_word[n+1]
            n = 0
            continue
        n += 1

    # 4단계
    if new_word:
        if new_word[0] == '.':
            del new_word[0]
    if new_word:
        if new_word[-1] == '.':
            del new_word[-1]

    # 5단계
    if not new_word:
        new_word.append('a')

    # 6단계
    if len(new_word) >= 16:
        new_word = new_word[0:15]

    if new_word[-1] == '.':
        del new_word[-1]

    # 7단계
    if len(new_word) <= 2:
        while len(new_word) <3:
            new_word.append(new_word[-1])

    answer = ''.join(new_word)
    return answer

print(solution('123_.def'))