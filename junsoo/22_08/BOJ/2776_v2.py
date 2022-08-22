'''
pypy기준
337604kb, 1508ms
'''

'''
nlist는 병합정렬
mlist 원소를 이진탐색
'''
'''
1
1
1
3
1 2 1
'''
import sys

t = int(input())
for i in range(t):
    n = int(input())
    nlist = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    mlist = list(map(int, sys.stdin.readline().split()))

    nlist.sort()

    for i in mlist:
                                                # [1 2 3 4 5] 5개
        start = 0                               #  s   m   e
        end = len(nlist) - 1                    #  s e
                                                #        s e
        while start <= end:
            mid = (start + end) // 2
            if i < nlist[mid]:              # 찾을 숫자가 중앙 값보다 작을 때
                end = mid - 1
            elif i > nlist[mid]:
                start = mid + 1
            elif i == nlist[mid]:
                print(1)
                break

        if start > end:
            print(0)

'''
차이점이 무엇인지?
함수를 따로 지정 하는 것이 시간 단축의 효과가 있는가?

파이썬3 기준
187744kb, 6384ms

import sys

def bs(li, n):
    s, e = 0, len(li) - 1
    while s <= e:
        m = (s + e) // 2
        if li[m] == n:
            return 1
        elif li[m] < n:
            s = m + 1
        else:
            e = m - 1
    return 0


for _ in range(int(input())):
    N = int(input())
    li1 = sorted(list(map(int, input().split())))
    M = int(input())
    li2 = list(map(int, input().split()))
    for n in li2:
        print(bs(li1, n))
'''



