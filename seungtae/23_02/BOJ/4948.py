import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    nums = [True for _ in range(2 * n + 1)]
    nums[1] = False

    double_n = 2 * n
    root_n = int((double_n)**0.5)

    for i in range(2, root_n+1):
        if nums[i]:
            j = i + i
            while j < double_n + 1:
                nums[j] = False
                j += i

    count = 0
    for i in range(n+1, double_n+1):
        if nums[i]:
            count += 1
    print(count)