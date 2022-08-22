def a(arr,x):
    first = 0
    last = len(arr) -1
    while True:
        if first > last:
            return -1
        idx = (first + last) //2 # 나머지는 버리고 시작
        if arr[idx] < x:
            first = idx + 1      # 작으면 앞에서 시작
        elif arr[idx] > x:
            last = idx -1        # 크면 뒤에서 시작
        else:
            return idx

T = int(input())
for t in range(T):
    t_case = int(input())
    t_arr = list(map(int,input().split()))
    case = int(input())
    arr = list(map(int,input().split()))
    t_arr.sort()
    for i in arr:
        if a(t_arr,i) >= 0:
            print(1)
        else:
            print(0)