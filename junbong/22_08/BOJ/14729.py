import sys


# 병합정렬 연습용, 시간초과로 pass는 안됨
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])                # 계속 반을 쪼개서 재귀로 들어감
    right = merge_sort(arr[mid:])               # 최초로 길이가 1인 배열이 반환됨

    merged = []                                 # left와 right의 원소들을 정렬해서 합친 배열
    l = r = 0                                   # 비교용 인덱스
    while l < len(left) and r < len(right):     # left 또는 right의 원소들을 모두 append할 때까지
        if left[l] < right[r]:                  # left와 right의 원소를 인덱스 기준으로 비교해 작은 것을 merged에 append
            merged.append(left[l])              # append하면 해당 배열의 인덱스를 증가시킴
            l += 1                              # 단순히 비교하면서 앞에서부터 순서대로 append해도 성립하는 이유는
        else:                                   # 합치기 전의 left와 right도 정렬되어 있는 상태이기 때문
            merged.append(right[r])
            r += 1
    
    merged += left[l:]                          # left 또는 right의 원소들을 모두 append 했다면
    merged += right[r:]                         # 나머지 right 또는 left의 남은 원소들을 append 해줌

    return merged


input = sys.stdin.readline
N = int(input().rstrip())
arr = [float(input().rstrip()) for _ in range(N)]
sorted_arr = merge_sort(arr)
for i in range(7):
    print(f'{sorted_arr[i]:.3f}')
