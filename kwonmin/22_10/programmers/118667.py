from collections import deque
def solution(queue1, queue2):

    q1 = sum(queue1)
    q2 = sum(queue2)
    if q1 == q2:
        return 0
    tot = q1 + q2
    if tot % 2:
        return -1
    avr = tot//2
    cnt = 0
    N = len(queue1)
    M = len(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while cnt < N*3 and queue1 and queue2:
        if q1 > q2:
            x = queue1.popleft()
            queue2.append(x)
            q1 -= x
            q2 += x
        else:
            x = queue2.popleft()
            queue1.append(x)
            q2 -= x
            q1 += x
        cnt += 1
        if q1 == q2:
            break
    if q1 != q2:
        return -1
    return cnt