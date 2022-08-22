import sys

T = int(input())
for tc in range(1, T+1):
    _ = input()
    a = list(map(int, sys.stdin.readline().split()))
    _ = input()
    b = list(map(int, sys.stdin.readline().split()))

    a.sort()

    for num in b:
        start = 0                   # 첫 시작점은 0
        end = len(a)                # 첫 끝점은 len(a)
        mid = len(a) // 2           # 중간값은 나누기 2 하고 소수점 버림
        while True:                     # 무한 루프!!
            if num == a[mid]:           # 중간값이 찾는 숫자랑 같으면 브레이크
                print('1')
                break
            if (end - start) == 1:      # 시작점, 끝점이 한칸차이가 되면 브레이크
                print('0')
                break

            # 위 쪽 두개의 if 문에서 break가 안되면 아래쪽 실행
            if num > a[mid]:                        # 찾는숫자가 반으로 자른 리스트의 위에 있으면 
                start = mid                             # 시작점을 올리고
                mid = ((end - start) // 2) + start      # 중간점 재설정
            else:                                   # 찾는숫자가 반으로 자른 리스트의 아래에 있으면
                end = mid                               # 끝점을 내리고
                mid = ((end - start) // 2) + start      # 중간점 재설정