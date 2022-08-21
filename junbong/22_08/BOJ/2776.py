# 220820
import sys

input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    # 이진 탐색을 하려면 탐색 대상이 되는 데이터는 정렬되어 있어야 함
    arr1 = sorted(list(map(int, input().split())))
    M = int(input().rstrip())
    arr2 = list(map(int, input().split()))

    for x in arr2:  # 이진 탐색
        result = 0
        s = 0
        e = N - 1
        while s <= e:
            mid = (s + e) // 2
            cur = arr1[mid]
            if cur > x:
                e = mid - 1
            elif cur < x:
                s = mid + 1
            else:
                result = 1
                break
        sys.stdout.write(str(result) + '\n')
