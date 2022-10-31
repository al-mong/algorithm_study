# 시작할 때 리스트 길이 2배로 하니 1번만 틀리고 3배로 하니 통과. 
# 무지성 큰곳에서 작은곳으로 요소 하나씩 던져주기 !

from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    length = len(q1)
    answer = 0

    sum1 = sum(q1)
    sum2 = sum(q2)

    while answer < length * 3:
        if sum1 == sum2:
            break

        if sum1 < sum2:
            x = q2.popleft()
            sum1 += x
            sum2 -= x
            q1.append(x)
        else:
            x = q1.popleft()
            sum1 -= x
            sum2 += x
            q2.append(x)

        answer += 1

    if answer == length * 3:
        return -1
    else:
        return answer