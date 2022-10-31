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