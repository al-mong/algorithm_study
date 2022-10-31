'''
하나의 큐에서 원소를 pop하면
무조건 다른 큐에 집어 넣음
=>
대소 비교 + 불가능 여부 판단만 하면 된다.
'''
from collections import deque


def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    sum_v = q1_sum + q2_sum
    if sum_v % 2:
        return -1
    length = len(queue1)
    answer = 0
    
    while q1_sum != q2_sum and answer <= 3 * length:
        if q1_sum > q2_sum:
            tmp = queue1.popleft()
            queue2.append(tmp)
            q1_sum -= tmp
            q2_sum += tmp
            answer += 1
        elif q1_sum < q2_sum:
            tmp = queue2.popleft()
            queue1.append(tmp)
            q2_sum -= tmp
            q1_sum += tmp
            answer += 1
            
    if answer == 3 * length + 1:
        return -1
            
    return answer
