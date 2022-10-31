from collections import deque


def solution(queue1, queue2):
    dequeue1, dequeue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    cnt = 0
    for _ in 300000:

        # 큐의 합이 같으면 멈춤
        if sum1 == sum2:
            return cnt

        # 합이 큰 것에서 하나 빼서 다른 큐에 넣기기
        if sum1 > sum2:
            tmp = dequeue1.popleft()
            dequeue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
            cnt += 1

        elif sum2 > sum1:
            tmp = dequeue2.popleft()
            dequeue1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
            cnt += 1

    return -1