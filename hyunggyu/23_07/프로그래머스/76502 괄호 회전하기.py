from collections import deque
def solution(s):
    answer = 0
    lst = deque(list(s))
    # [] 이렇게 닫히게 되면 닫힌 것 안에서 개행과 폐행이 이루어져야 한다.
    for i in range(len(s)):
        visited = []
        flag = 1
        for j in range(len(s)):
            if lst[j] in ["[","{","("]:
                visited.append(lst[j])
            else:
                if visited:
                    tmp = visited.pop()
                    if tmp == "(" and lst[j] == ")":
                        continue
                    elif tmp == "[" and lst[j] == "]":
                        continue
                    elif tmp == "{" and lst[j] == "}":
                        continue
                    else:
                        # 짝이 맞지 않은 경우 fail
                        flag = 0
                        break                        
                else:
                    # 폐행이 먼저 온 경우 return fail
                    flag = 0
                    break
        if flag and not visited:
            # visited 안에 값이 존재하지 않을 때 완성
            answer += 1
        lst.rotate(1)
    return answer