com = int(input())
T = int(input())
sorted_list=[]
for t in range(T):
    a=tuple(map(int,input().split()))
    if a[0]>a[1]:
        c = list(a)[::-1]
    sorted_list.append(a)
sorted_list.sort()
count = 0
print(sorted_list)

    
