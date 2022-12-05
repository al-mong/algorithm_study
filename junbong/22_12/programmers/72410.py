from collections import deque


def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # 2 ~ 4단계
    stack = deque()
    for i in range(len(new_id)):
        char = new_id[i]
        if char.isdigit() or 97 <= ord(char) <= 122 or char in {'0', '-', '_', '.'}:  # 2단계
            if not stack and char == '.':  # 4단계
                continue
            if stack and stack[-1] == '.' and char == '.':  # 3단계
                continue
            stack.append(char)
    while stack and stack[-1] == '.':  # 4단계
        stack.pop()
    
    # 5단계
    if not stack:
        stack.append('a')
    
    # 6단계
    while len(stack) >= 16 or stack[-1] == '.':
        stack.pop()
    
    # 7단계
    while len(stack) <= 2:
        stack.append(stack[-1])
    
    answer = ''.join(list(stack))

    return answer


print(solution('.1@@##23_.DefFS.'))
