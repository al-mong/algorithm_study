# 220805
import sys
from collections import deque

# 함수도 객체이므로 아래와 같이 저장 가능
input = sys.stdin.readline  # 더 빠르게 입력

for _ in range(int(input().rstrip())):  # readline은 개행문자 '\n'을 포함하기 때문에 rstrip으로 없애줘야 함
    line = input().rstrip()
    stack = deque()
    flag = False  # 여는 괄호 전에 닫는 괄호 기호가 먼저 나왔는지 확인할 boolean
    for p in line:
        if p == '(':
            stack.append(p)
        else:
            try:
                stack.pop()
            except:  # 예외시 실행할 부분
                flag = True
                break  # 더 이상 볼 필요 없으므로 break

    if flag or len(stack):  # 열리지도 않은 괄호를 닫으려 했거나, 열린 괄호를 다 닫지 않았으면
        print("NO")
        continue

    print("YES")
