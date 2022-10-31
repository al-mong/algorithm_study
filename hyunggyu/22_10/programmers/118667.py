from collections import deque
def solution(queue1, queue2):
    l = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    a = sum(queue1)
    b = sum(queue2)

    if (a+b)%2:
        answer = -1
        return answer
    else:
        cnt = 0
        while True:
            if cnt > l*2+1 or not queue1 or not queue2:
                answer = -1
                return answer
            if a < b:
                aplus = queue2.popleft()
                a += aplus
                b -= aplus
                queue1.append(aplus)
                cnt += 1
            elif a > b:
                bplus = queue1.popleft()
                a -= bplus
                b += bplus
                queue2.append(bplus)
                cnt += 1
            else:
                break
        answer = cnt
        return answer
