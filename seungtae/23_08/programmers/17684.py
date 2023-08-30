from collections import defaultdict

def solution(msg):
    answer = []
    d = defaultdict(int)
    num = 27

    for i in range(65, 91):
        d[chr(i)] = i-64

    index = 0

    while index < len(msg):

        # 가장 긴 압축단어 찾기 --------- 여기부터
        word = ""
        maxWord = ""
        maxIndex = 0
        for i in range(index, len(msg)):
            word += msg[i]
            if d[word]:
                maxWord = word
                maxIndex = i
        # -------------- 여기까지

        answer.append(d[maxWord])

        # 압축단어 찾은 곳 다음으로 인덱스 옮겨주고 뒤에 더 있으면 압축단어 + 다음단어를 압축단어로 추가
        index = maxIndex + 1
        if index != len(msg):
            d[maxWord+msg[index]] = num
            num += 1

    return answer