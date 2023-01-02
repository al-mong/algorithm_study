# 230102
from collections import deque


def solution(number, k):
    stack = deque([int(number[0])])

    for i in range(1, len(number)):
        dg = int(number[i])
        while stack and dg > stack[-1] and k > 0:  # 앞 자리 숫자가 커야하므로
            stack.pop()
            k -= 1
        stack.append(dg)

    # 제거 횟수가 남은 경우, 뒷 부분을 자름 - 더 작은 숫자가 뒤에 붙었다는 뜻이므로
    while k > 0:
        stack.pop()
        k -= 1
    
    answer = ''.join(map(str, stack))
    
    return answer


print(solution("4321", 1))
