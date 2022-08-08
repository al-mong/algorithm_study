# 실버4. 괄호
# 승태한테 좀 물어보고 그래도 내가 풀었음 ㅎㅎㅎ 캬
# 감격임 ㅋㅋㅋ
test_case = int(input())

for i in range(test_case):
    stack = list(input())
    stack_a = []
    isprint = False
    for c in stack:                                             
        if c == '(':
            stack_a.append(c)
        elif c == ')':
            if stack_a:
                stack_a.pop()
            else:
                print('NO')
                isprint = True
                break
    if isprint == False:                
        if stack_a:
            print('NO')
        else:
            print('YES')
