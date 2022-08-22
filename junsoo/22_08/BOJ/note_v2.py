def Factorial(n):
    if n == 1:
        print(1, f'facto {1}')
        return 1
    else:
        print(n * Factorial(n-1), f'facto {n}')
        return n * Factorial(n-1)

Factorial(3)
'''
Factorial(3)
= 3 * Factorial(2)
= 3 * 2 * Factorial(1)
= 3 * 2 * 1
'''