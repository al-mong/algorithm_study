# n~ 2n 사이 소수 개수 세기
import sys
input = sys.stdin.readline

mx_n = 123456*2
arr = [0] + [1]*mx_n
arr[1] = 0
    # 소수면 0 소수가 아니면 1
for i in range(2,mx_n + 1):
    if arr[i] == 1:
        tmp = 2
        flag = True
        while flag:
            try:
                arr[i*tmp] = 0
                tmp += 1
            except:
                flag = False
while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        print(sum(arr[n:2*n+1]))
    # 1 ~ 123456

                
