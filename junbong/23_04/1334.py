# 230422
n = input()
n_len = len(n)

if n_len == 1:
    if n == '9':
        print(11)
    else:
        print(int(n) + 1)
else:
    if n_len % 2 == 0:  # 짝수 자릿수
        left = n[:n_len // 2]  # 왼쪽
        right = n[n_len // 2:]  # 오른쪽
        if left[::-1] > right:  # 왼쪽을 뒤집은게 오른쪽보다 크면
            print(left + left[::-1])
        else:  # 오른쪽이 더 크면
            left = str(int(left) + 1)  # 왼쪽에 + 1 (왼쪽에 제일 작게 더하는 과정)
            if len(left) > n_len // 2:  # 왼쪽 숫자가 9로만 이루어진 경우 ex) 999
                print(left + left[::-1][1:])  # 자릿수가 하나 올라가므로 0 하나 빼야함
            else:
                print(left + left[::-1])
    else:  # 홀수 자릿수
        left = n[:n_len // 2]
        middle = n[n_len // 2]
        right = n[n_len // 2 + 1:]
        if left[::-1] > right:
            print(left + middle + left[::-1])
        else:
            middle = str(int(middle) + 1)  # 제일 작게 더할 수 있는 부분이 가운데 부분이므로
            if len(middle) > 1:  # middle이 9였을 때
                middle = '0'
                tmp = len(left)
                left = str(int(left) + 1)
                if (len(left) > tmp):  # left와 right가 9로만 이루어져있었을 때
                    middle = ''
            print(left + middle + left[::-1])
