'''
1. 주어진 수를 이진수로 바꾼다.
5 -> 101
42 -> 101010

2. 바뀐 이진수 길이가 원래 길이보다 같거나 큰 최소 2^n - 1이 될 때까지 앞에 0을 추가한다.
101
0101010

3. 부모 노드가 0(더미 노드)일 때 자식 노드가 1이면 X
'''

# 이진수 길이가 원래 길이보다 같거나 큰 최소 2^n - 1이 될 때까지 앞에 0을 추가


def to_perfect(b):
    b_len = len(b)
    t_len = 1
    weight = 1

    while t_len < b_len:
        weight *= 2
        t_len += weight

    return '0' * (t_len - b_len) + b


# 트리에서 부모노드가 0일 때, 자식 노드가 1인 경우 탐색
def dfs(pb):
    # 리프노드에 도착
    if len(pb) == 1:
        return 1

    half = len(pb) // 2
    root = pb[half]
    left, right = pb[:half], pb[half + 1:]

    if root == '0' and (left[len(left) // 2] == '1' or right[len(right) // 2] == '1'):
        return 0

    return dfs(left) and dfs(right)


def solution(numbers):
    answer = []

    for number in numbers:
        b = bin(number)[2:]
        pb = to_perfect(b)
        answer.append(dfs(pb))

    return answer


print(solution([7, 42, 5]))
print(solution([63, 111, 95]))