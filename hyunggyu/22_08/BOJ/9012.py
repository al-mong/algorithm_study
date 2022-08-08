T = int(input())
for t in range(T):
    a = input()
    if a == '':
        print('YES')
    else:
        b = 0
        for i in a:
            if b<0:
                b= -1
                break
            elif i == '(':
                b += 1
            else:
                b -= 1
        if b == 0:
            print('YES')
        else:
            print('NO')
        
