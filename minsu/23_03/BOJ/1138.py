n = int(input())
arr = list(map(int, input().split()))
order = [0] * len(arr)

for i in range(len(arr)):
    cnt = 0
    for j in range(len(order)):
        if order[j] == 0:
            cnt +=1
            if cnt == arr[i] + 1:
                order[j] = i+1
                break

for k in order:
    print(k, end=' ')