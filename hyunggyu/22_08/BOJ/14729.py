def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:          # 크기가 2보다 작으면 반환
            return
        mid = (low + high) // 2     # 반으로 나누기
        sort(low, mid)              # 작은 쪽 sort
        sort(mid, high)             # 큰 쪽 sort
        merge(low, mid, high)       # 합치기

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high: # 하나씩 비교해서 큰것 작은것 분류
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))
T = int(input())
student = []
for t in range(T):
    student.append(float(input()))
merge_sort(student)
student = student[:7]
for t in range(7):
    print('{:.3f}'.format(student[t]))
