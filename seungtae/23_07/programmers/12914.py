import sys
sys.setrecursionlimit(100000)

def solution(n):
    def count_permutations_without_repetition(n, r):
        # 중복제거 순열 갯수 계산 함수
        total_elements = n + r
        numerator = factorial(total_elements)
        denominator = factorial(n) * factorial(r)
        return numerator // denominator

    def factorial(n):
        # 팩토리얼 계산 함수
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    answer = 0
    r = 0

    while n >= 0:
        result = count_permutations_without_repetition(n, r)
        answer += result

        n -= 2
        r += 1

    return answer % 1234567

print(solution(2000))
print(solution(4))
print(solution(3))