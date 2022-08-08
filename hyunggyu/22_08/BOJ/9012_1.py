T = int(input())
for t in range(T):
    stack = []
    count = 0
    data = list(input())
    for i in data:
        stack.append(i)
        if stack[-1] == ')':
            if len(stack) == 1:
                stack.append('GG')
                break
            elif stack[-2] == '(':
                stack.pop()
                stack.pop()            
            else:
                stack.append('GG')
                break
    if stack == []:
        print('YES')
    else:
        print('NO')
