from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    result = 0
    n, m = map(int, input().split())
    important = deque(map(int, input().split()))
    for i in range(n):
        important[i] = (important[i], i)  # important = [(받은 숫자, 원래 위치인덱스), ...)

    # 제일 앞에 것을 꺼내서 가장 큰지 확인
    while important:
        my_max = max(important)[0]
        a = important.popleft()
        if a[0] == my_max:
            result += 1
            if a[1] == m: # 원하는 인덱스값이 나오면 break
                break
        else:
            important.append(a)
    print(result)


