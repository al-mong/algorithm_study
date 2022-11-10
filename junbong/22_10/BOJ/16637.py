# 221107
import sys; input = sys.stdin.readline;
from collections import deque


def calculate(x, oper, y):
    if oper == '+':
        return int(x) + int(y)
    elif oper == '-':
        return int(x) - int(y)
    elif oper == '*':
        return int(x) * int(y)


def sol(subset):
    digits_copy = deque(map(int, digits[:]))
    operators_copy = deque(operators[:])
    q = deque()
    i = 0
    while i < N // 2:
        if i == 0:
            q.append(digits_copy.popleft())
            q.append(operators_copy.popleft())
        else:
            if subset[i]:
                q.append(calculate(q.popleft(), q.popleft(), calculate(digits_copy.popleft(), operators_copy.popleft(), digits_copy.popleft())))
                if operators_copy:
                    q.append(operators_copy.popleft())
                i += 1
            else:
                q.append(calculate(q.popleft(), q.popleft(), digits_copy.popleft()))
                q.append(operators_copy.popleft())
        i += 1

    if digits_copy:
        q.append(calculate(q.popleft(), q.popleft(), digits_copy.popleft()))

    return q[0]

        
def make_subset(n, idx, subset):
    global result
    if idx == n:
        result = max(sol(subset), result)
    else:
        if subset[idx] == 0:
            make_subset(n, idx + 1, subset + [1])
            make_subset(n, idx + 1, subset + [0])
        else:
            make_subset(n, idx + 1, subset + [0])


N = int(input().rstrip())
exp = input().rstrip()
if N == 1:
    print(int(exp[0]))
    exit()
subsets = []
digits = []
operators = []
result = -(2 ** 31)

for i in range(N):
    if i % 2:
        operators.append(exp[i])
    else:
        digits.append(exp[i])

make_subset(N // 2 - 1, 0, [0])

print(result)
