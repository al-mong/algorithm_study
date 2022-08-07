# 220805
import sys
from collections import deque

'''
1. 스택 문제인 이유
닫는 괄호가 나오면 가장 최근의 여는 괄호가 닫힌다.
스택의 개념인 후입선출-LIFO(Last In First Out) 방식.

2. 풀이
여는 괄호가 나오면 스택에 넣고, 닫는 괄호가 나오면 뺀다.
여는 괄호의 개수 초과로 닫는 괄호가 나오는 '순간' 괄호 문자열이 아니게 되므로 NO 출력.
문자열을 '다 탐색한 이후' 여는 괄호의 개수 미만으로 닫는 괄호가 나오면
괄호 문자열이 아니므로 NO 출력.
이외에는 (여는 괄호가 먼저 나오면서, 닫는 괄호와 개수가 같으면) YES를 출력한다.
'''

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
            try:  # 속도 측면에서 if보다 빠르다고 생각해서 사용
                stack.pop()
            except:  # 예외시 실행할 부분
                flag = True
                break  # 더 이상 볼 필요 없으므로 break

    # 열리지도 않은 괄호를 닫으려 했거나, 열린 괄호를 다 닫지 않았으면
    if flag or len(stack):
        print("NO")
        continue

    print("YES")
