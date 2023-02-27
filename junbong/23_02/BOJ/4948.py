# 230227
import sys

input = sys.stdin.readline

MAX = 123456 * 2 + 1
is_prime_list = [1] * (MAX)

for i in range(2, MAX):
    if is_prime_list[i] == 1:
        for j in range(2, (MAX - 1) // i + 1):
            is_prime_list[i * j] = 0

while True:
    n = int(input())

    if n == 0:
        break

    cnt = 0
    for i in range(n + 1, n * 2 + 1):
        if is_prime_list[i]:
            cnt += 1

    print(cnt)
