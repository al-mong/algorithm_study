def pp(k):
    p_list = [False, False, True] + [True, False] * (k-1)
    for num, v in enumerate(p_list):
        if num > 2 and v:
            for j in range(2, (2*k)//num +1):
                p_list[num*j] = False
    return p_list


num_list = pp(123456)

while True:
    n = int(input())
    if n == 0:
        break
    result = 0
    for num, v in enumerate(num_list):
        if num > 2*n:
            break
        if num > n and v:
            result = result + 1

    print(result)