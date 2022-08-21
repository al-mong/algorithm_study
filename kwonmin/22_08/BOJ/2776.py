# 이진탐색을 이용하여 구현
# 미리 이진탐색 메커니즘을 이용한 함수를 만들어서 풀기
# 필요한 값 생각하기 : 목표값, 시작/끝값
# 재귀로 풀 때 생각해야 할 것 : 중간점의 위치를 +1 / -1 해주는 것.
def binary_search(point,start,end):
    if start > end:
        return 0
    else:
        mid = (start + end) // 2
        if point == nums1[mid]:
            return 1
        elif point < nums1[mid]:
            return binary_search(point, start, mid-1)
        elif point > nums1[mid]:
            return binary_search(point, mid+1, end)

T = int(input())
for _ in range(T):
    N = int(input())
    nums1 = list(map(int,input().split()))
    nums1.sort() # 이진탐색을 하기 위해서 오름차순으로 정렬
    M = int(input())
    nums2 = list(map(int,input().split()))
    # 시작은 0, 끝은 N-1로 시작.
    for num in nums2:
        print(binary_search(num, 0, N-1))