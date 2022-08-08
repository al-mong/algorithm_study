t = int(input())

for i in range(t):
    list_left = []                      # 좌측 스택, '('를 받음
    list_right = []                     # 우측 스택, ')'를 받음
    data = input()                      # 데이터 전체 받기

    for k in data:
        if k == '(':
            list_left.append(k)
        else:
            if list_left != []:
                list_left.pop()
            else:
                list_right.append(k)    # 우측에 받을 때, 좌측 스택에 값이 있으면 좌측 유지. 우측 제거

    if list_left == [] and list_right == []:
        print('YES')
    else:
        print('NO')