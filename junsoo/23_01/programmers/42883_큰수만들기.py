from collections import deque

def solution(number, k):
    # 기존 숫자 리스트
    num_dict = {i: deque([]) for i in range(10)}
    num_dict[int(number[0])].append(0)

    length = len(number)
    K = k

    idx = 0
    while k and idx < length - 1:
        idx += 1
        # 비교할 숫자
        new = number[idx]   # str

        for i in range(int(new)):   # 비교할 숫자보다 작은 숫자들 전부 제거
            while k:
                if num_dict.get(i):
                    num_dict[i].popleft()
                    k -= 1
                else:
                    break

        num_dict[int(new)].append(idx)
        # print(num_dict)

    result = ['' for i in range(length)]
    for key, v in num_dict.items():
        for i in v:
            result[i] = str(key)
    # print(result)

    answer = ''
    for i in result:
        answer += i
    if idx != length - 1:
        answer += number[idx+1:]
    # print(answer)
    return answer[:length - K]

print(solution('1924', 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))