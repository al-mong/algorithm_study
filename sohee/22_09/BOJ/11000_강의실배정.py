import sys
input = sys.stdin.readline

'''하나하나 탐색하는걸로 하면 시간초과 백빵 뜸...
일단 강의 시작시간, 종료시간을 나눠서 arr 에 추가하기
시작시간은 1이랑 튜플로, 종료시간은 0이랑 튜플로..
그리고 arr 정렬하고 시작시간일 때는 cnt 에 1 추가하고
종료시간일 때는 cnt 에서 1을 뺌
그리고 최대 cnt 구하면 됨. 강의실을 그만큼 쓰고 있다는 의미'''

N = int(input())
arr = []
for i in range(N):
    s, e = map(int, input().split())
    arr.append((s, 1))
    arr.append((e, 0))

arr.sort()
cnt = 0
maxV = 0
for i in range(2*N):
    if arr[i][1] == 1:
        cnt += 1
    else:
        cnt -= 1
    if cnt > maxV:
        maxV = cnt

print(maxV)





