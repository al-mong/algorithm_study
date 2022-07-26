# [입력]
# 입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 
# 력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 
# 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다.
# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(

# [출력]
# 출력은 표준 출력을 사용한다. 
# 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 
# NO
# NO
# YES
# NO
# YES
# NO

# 자료구조 스택으로 풀기 - Last In First Out 후입선출

# 빈 리스트를 만들고 '(' 가 들어오면 리스트에 append, ')' 가 들어오면 리스트에 들어있던 '('를 pop() 한다.
# VPS가 아닌 경우는 2가지로 요약한다.
# 1. for 문을 다 돌고 난 후 리스트의 길이가 0이 아닐 때
# 2. pop을 할 '(' 가 없는데 ')'가 들어온 경우 리스트의 길이를 증가시키고 for문을 탈출(break)
# for 문을 다 돌고 나서 길이를 쟀을 때 길이가 0이면 VPS, 1이상이면 not VPS이다  

T = int(input())

for test_case in range(T):
    ps = list(input())
    vps = []
    for p in ps:
        if p == '(':
            vps.append(p)
        else:
            if len(vps) == 0:
                vps.append(1)
                break
            else:
                vps.pop()
    
    if len(vps):
        print("NO")
    else:
        print("YES")