from collections import deque

def solution(queue1, queue2):
    s1 = sum(queue1)
    s2 = sum(queue2)

    total = s1 + s2
    if total % 2:
        return -1

    n = len(queue1)     # 시행 횟수용 길이

    queue1, queue2 = deque(queue1), deque(queue2)

    half = total//2

    answer = 0

    difference = s1 - s2

    while answer <= 3*n:
        if difference > 0:          # s1이 더 큼
            tmp = queue1.popleft()
            queue2.append(tmp)
            difference -= 2 * tmp
            answer += 1

        elif difference < 0:        # s2가 더 큼
            tmp = queue2.popleft()
            queue1.append(tmp)
            difference += 2 * tmp
            answer += 1

        elif difference == 0:
            return answer

    return -1



print(solution([1,1,1,9,1], [1,1,1,1,1]))