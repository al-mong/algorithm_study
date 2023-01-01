def solution(number, k):

    count = 0
    i = 0
    stack = []

    while count != k:
        # 마지막 인덱스까지 탐색 했으면 스택의 끝에서부터 pop하기
        if i == len(number):
            stack.pop()
            count += 1
            continue

        # 스택이 비어있으면 숫자 넣기
        if not stack:
            stack.append(int(number[i]))
            i += 1
            continue

        # 다음 숫자가 스택 마지막 숫자보다 크면 스택에서 삭제하기
        if int(number[i]) > stack[-1]:
            stack.pop()
            count += 1
        #  아니면 다음 숫자 탐색하러 가기
        else:
            stack.append(int(number[i]))
            i += 1

    # 남은 숫자들 모으기
    for res in range(i, len(number)):
        stack.append(int(number[res]))

    answer = "".join(list(map(str, stack)))
    return answer

if __name__ == '__main__':
    print(solution("1924", 2))
    print(solution("1231234", 3))
    print(solution("4177252841", 4))