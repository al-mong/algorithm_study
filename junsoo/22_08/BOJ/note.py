def FactorialTail(n, acc):
    if n == 1:
        print(acc, f'facto {1}')
        return acc
    else:
        print(FactorialTail(n - 1, acc * n), f'facto {n}')
        return FactorialTail(n - 1, acc * n)

def Factorial(n):
    print(FactorialTail(n, 1), f'facto {n}')
    return FactorialTail(n, 1)

Factorial(3)